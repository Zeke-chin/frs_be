from sqlalchemy import Column, Integer, String, Float

from app.models.database import BaseModel


class Human(BaseModel):
    __tablename__ = "human"
    id = Column(Integer, primary_key=True, index=True, comment='id')
    name = Column(String(255), comment='姓名')
    temperature = Column(Float, comment='最后一次体温')
    create_time = Column(Integer, comment='创建时间')
    update_time = Column(Integer, comment='更新时间')

