from sqlalchemy import Column, Integer, String
from Database import Base

class User(Base):
    __tablename__ = "users"

    Id = Column(Integer,primary_key=True, index=True)
    Name = Column(String)
    Email = Column(String)
    Nickname = Column(String)