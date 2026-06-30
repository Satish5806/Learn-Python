from datetime import datetime, timezone
from sqlalchemy import Column, DateTime
from sqlalchemy.orm import declarative_base
from main import session

Model = declarative_base()
Model.query = session.query_property()


class TimeStampedModel(Model):
    __abstract__ = True
    
    created_at = Column(
        DateTime, 
        default=lambda: datetime.now(timezone.utc)
    )
    
    updated_at = Column(
        DateTime, 
        onupdate=lambda: datetime.now(timezone.utc)
    )