from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import relationship

from src.common.database.database_engine import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True) # TODO Integer to UUID
    name = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String) # TODO - remove it after testing
    is_active = Column(Boolean, default=True)

