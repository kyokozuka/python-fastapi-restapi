from dataclasses import dataclass
from sqlalchemy import Column, Integer, String

from src.infrastructure.database.mysql import Base


@dataclass
class User(Base):
    __tablename__ = 'users'
    
    email: str = Column(String(128), primary_key=True)
    first_name: str = Column(String(128))
    last_name: str = Column(String(128))
    first_name_kana: str = Column(String(128))
    last_name_kana: str = Column(String(128))
    gender: int = Column(Integer)
    address: str = Column(String(255))
    
    def __repr__(self):
        return '<User %r>' % self.email