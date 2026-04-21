from app.api.v1.repositories.base import BaseRepository
from app.api.v1.models import Product

__model__ = Product

class ProductRepository(BaseRepository):
    def __init__(self, db):
        super().__init__(db, __model__)

    def get_by_name(self, name:str):
        return self.db.query(__model__).filter(
            __model__.name==name
            ).first()