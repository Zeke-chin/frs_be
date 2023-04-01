from typing import Union,Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class UserCreate(BaseModel):
    name: str
    head_img: str
    email: str

    class Config:
        schema_extra = {
            "example": {
                "name": faker.name(),
                "head_img": "图片地址",
                "email": faker.email(),
            }
        }


class UserUpdate(BaseModel):
    name: Optional[str] = None

    class Config:
        schema_extra = {
            "example": {
                "name": faker.name(),
            }
        }


class UserGet(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    email: Optional[str] = None
    create_time: Optional[int] = None
    update_time: Optional[int] = None
    last_auth_time: Optional[int] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": faker.name(),
                "email": faker.email(),
                "create_time": 1620000000,
                "update_time": 1620000000,
                "last_auth_time": 1620000000,
            }
        }



class User(BaseModel):
    id: int
    name: str
    head_img: str
    email: str
    create_time: int
    update_time: int
    last_auth_time: int

    class Config:
        orm_mode = True
