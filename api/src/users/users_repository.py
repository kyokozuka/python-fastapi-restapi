from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:
    
    def __init__(self, db: Session):
        self.db = db
        
    def find_all(self):
        return self.db.query(User).all()
    
    def find_by_email(self, email: str) -> User:
        return self.db.query(User).filter(User.email == email).first()
    
    def create(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        
    def delete(self, user: User):
        self.db.delete(user)
        self.db.commit()