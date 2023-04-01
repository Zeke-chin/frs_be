from sqlalchemy import Column, Integer, String

from app.models.database import BaseModel


class User(BaseModel):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='用户名', unique=True)
    head_img = Column(String(255), comment='头像')
    email = Column(String(255), comment='邮箱', unique=True)
    create_time = Column(Integer, comment='创建时间')
    update_time = Column(Integer, comment='更新时间')
    last_auth_time = Column(Integer, comment='最近时间')
