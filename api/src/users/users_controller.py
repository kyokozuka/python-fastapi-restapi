from sqlalchemy.orm import Session
from fastapi import Depends

from src.schemas.user import User, UserDel
from src.infrastructure.database.mysql import get_db
from src.users.users_service import UserService
from src.users.users_repository import UserRepository


class UserController:
    
    def build(self, db: Session):
        user_repo = UserRepository(db)
        self.user = UserService(repo=user_repo)
    
    async def users(self, db: Session = Depends(get_db)):
        self.build(db)
        results = self.user.find_all()
        return results
    
    async def add_todo(self, data: User, db: Session = Depends(get_db)):
        self.build(db)
        return self.user.create(data=data)
    
    async def update_todo(self, data: User, db: Session = Depends(get_db)):
        self.build(db)
        return self.user.update(data=data)
    
    async def remove_todo(self, data: UserDel, db: Session = Depends(get_db)):
        self.build(db)
        self.user.delete(email=data.email)
        return True