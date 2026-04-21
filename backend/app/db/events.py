from sqlalchemy import event
from sqlalchemy.orm import Session

@event.listens_for(Session, "before_flush")
def soft_delete(session, flush_context, instances):
    for obj in session.deleted:
        if hasattr(obj, "is_deleted"):
            obj.is_deleted = True
            session.add(obj)