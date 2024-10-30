from typing import Optional
from typing import List
from pydantic import BaseModel, EmailStr


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


class UserInDBBase(UserBase):
    id: Optional[int] = None

    class Config:
        orm_mode = True

class Item(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True  # 确保 Pydantic 可以接受 ORM 对象

# 更新 User schema，添加 items 字段
class User(UserInDBBase):
    items: List[Item] = []  # 添加 items 字段

    class Config:
        orm_mode = True

# Additional properties stored in DB
class UserInDB(UserInDBBase):
    hashed_password: str
