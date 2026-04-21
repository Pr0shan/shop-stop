from app.db.session import SessionLocal
from app.db.transaction import transaction
def get_transactional_db():
    db = SessionLocal()
    try:
        with transaction(db):
            yield db
    finally:
        db.close()