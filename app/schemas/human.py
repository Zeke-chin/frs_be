from typing import Union

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')

class HumanCreate(BaseModel):
    name: str

    class Config:
        schema_extra = {
            "example": {
                "name": faker.name()}}

class HumanGet(BaseModel):
    name: Union[str, None] = None
    create_time: Union[int, None] = None
    update_time: Union[int, None] = None

class HumanUpdate(BaseModel):
    name: Union[str, None] = None
    temperature: Union[float, None] = None

    class Config:
        schema_extra = {
            "example": {
                "name": faker.name(),
                "temperature": 36.1}}

class Human(BaseModel):
    id: int
    name: str
    temperature: float
    create_time: int
    update_time: int

    class Config:
        orm_mode = True


