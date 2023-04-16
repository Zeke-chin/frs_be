from typing import Union,Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class LogerLine(BaseModel):
    date: int
    level: str
    message: str
