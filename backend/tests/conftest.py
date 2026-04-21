import pytest
from sqlalchemy import create_engine, event
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker
from app.db.base import Base
from app.api.v1.models import User, Product, ProductStatus

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)

TestingSessionLocal = sessionmaker(bind=engine)

@event.listens_for(Engine, "connect")
def enable_sqlite_fk(dbapi_connection, connection_record):
    cursor=dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    session = TestingSessionLocal()

    try:
        yield session
    finally:
        session.close()
        Base.metadata.drop_all(bind=engine)

@pytest.fixture
def user(db):
    user = User(
        name="test_user",
        email="test_user@test.com",
        role="seller"
    )
    db.add(user)
    db.flush()

    return user

@pytest.fixture
def product_factory(db, user):
    def create_product(**kwargs):
        product = Product(
            slug=kwargs.get("slug", "default_slug"),
            name=kwargs.get("name", "defualt_name"),
            owner_id=user.id
        )
        db.add(product)
        db.flush()
        return product

    return create_product

@pytest.fixture
def product_data_factory(user):
    def product_data(**kwargs):
        return {
            "slug": kwargs.get("slug", "test_product"),
            "name": kwargs.get("name", "Test Product"),
            "owner_id": user.id,
            "status": ProductStatus.ACTIVE
        }