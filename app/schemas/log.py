from typing import Union,Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class Loger(BaseModel):
    data: int
    level: str
    message: str
