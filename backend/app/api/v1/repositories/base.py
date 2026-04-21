from typing import Type, List, Optional
from sqlalchemy.orm import Session

class BaseRepository:
    def __init__(self, db:Session, model:Type):
        self.db = db
        self.model = model

    def get(self, id:int):
        return self.db.query(self.model).filter(
            self.model.id == id
            ).first()
    
    def list(self, skip: int = 0, limit:int = 0):
        return self.db.query(
            self.model
            ).offset(skip).limit(limit).all()
    
    def create(self, obj_in):
        self.db.add(obj_in)
        self.db.flush()
        return obj_in
    