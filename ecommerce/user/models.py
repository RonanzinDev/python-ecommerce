from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from ecommerce.db import Base
from . import hashing

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    email = Column(String(255), index=True)
    password = Column(String(255))
    
    def __init__(self, name: str, email: str, password: str, *args, **kwargs):
        self.name = name
        self.email = email
        self.password = hashing.hash_password(password)
        
    def check_password(self, password: str) -> bool:
        return hashing.verify_password(self.password, password)