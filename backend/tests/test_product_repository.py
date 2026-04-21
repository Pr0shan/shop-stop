from app.api.v1.repositories.product import ProductRepository
from app.api.v1.models import Product, ProductStatus
import pytest
from sqlalchemy.exc import IntegrityError

def test_create_product(db, product_data_factory):
   repo = ProductRepository(db)

   product = Product(**product_data_factory)
   result = repo.create(product)

   assert result.id is not None
   assert result.status==ProductStatus.ACTIVE

@pytest.mark.parametrize("missing_field", [
   "slug",
   "name",
   "owner_id"
   ])
def test_product_missing_required_fields(db, product_data, missing_field):
   repo = ProductRepository(db)
   data = product_data
   data[missing_field] = None
   product = Product(**data)

   with pytest.raises(IntegrityError):
      repo.create(product)
      db.commit()

@pytest.mark.parametrize("common_name_field",["slug", "name"])
def test_product_uniqueness(db, product_data, common_name_field):
   repo = ProductRepository(db)
   data_1 = {
      "slug": "test_product",
      "name": "test Product",
      "owner_id": user.id,
      "status": ProductStatus.ACTIVE
   }
   data_1[common_name_field] = "common_name"
   product_1 = Product(**data_1)

   data_2 = {
      "slug": "test_product",
      "name": "test Product",
      "owner_id": user.id,
      "status": ProductStatus.ACTIVE
   }
   data_2[common_name_field] = "common_name"
   product_2 = Product(**data_2)
   with pytest.raises(IntegrityError):
      repo.create(product_1)
      repo.create(product_2)
      db.commit()

def test_product_get_by_name(db, user):
   pass