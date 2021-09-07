from pydantic import BaseModel


class User(BaseModel):
    email: str
    first_name: str
    last_name: str
    first_name_kana: str
    last_name_kana: str
    gender: int
    address: str
    
    class Config:
        orm_mode = True
        
class UserDel(BaseModel):
    email: str
    
    class Config:
        orm_mode = True