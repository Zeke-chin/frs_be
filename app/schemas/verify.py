from typing import Union, Optional

from pydantic import BaseModel
from faker import Faker

faker = Faker(locale='zh_CN')


class VerifyPost(BaseModel):
    source_path: str
    target_path: str

    class Config:
        schema_extra = {
            "example": {
                "source_path": "源图片",
                "target_path": "目标图片"
            }
        }
