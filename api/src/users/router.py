from typing import List

from fastapi import APIRouter

from src.users.users_controller import UserController
from src.schemas.user import User
from src.models.user import User as UserModel


user_app = APIRouter(prefix='/api/user', tags=['User'],
                     responses={404: {'description': 'Not found'}})

user = UserController()

user_app.add_api_route('/', endpoint=user.users, methods=['GET'], response_model=List[User])
user_app.add_api_route('/add', endpoint=user.add_todo, methods=['POST'], response_model=User)
user_app.add_api_route('/update', endpoint=user.update_todo, methods=['PUT'], response_model=User)
user_app.add_api_route('/del', endpoint=user.remove_todo, methods=['DELETE'])