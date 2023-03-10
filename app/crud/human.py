import threading
import time
from typing import List

import requests

from app import models, schemas
from sqlalchemy.orm import Session
from app.crud.basic import update_to_db


def create_human(db: Session, item: schemas.HumanCreate):
    # sourcery skip: use-named-expression
    # 创建
    db_item = models.Human(**item.dict(), **{'create_time': int(time.time())})
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_human(db: Session, item_id: int, update_item: schemas.HumanUpdate):
    return update_to_db(update_item=update_item, db=db, item_id=item_id, model_cls=models.Human)


def get_human_once(db: Session, item_id: int):
    if item := db.query(models.Human).filter(models.Human.id == item_id).first():
        return item
    else:
        raise Exception(f"人物id {item_id} 不存在")


def get_human(db: Session, item: schemas.HumanGet):
    db_query = db.query(models.Human)
    if item.name:
        db_query = db_query.filter(models.Human.name.like(f"%{item.name}%"))
    if item.update_time:
        db_query = db_query.filter(models.Human.update_time <= item.update_time)
        db_query = db_query.filter(models.Human.update_time >= item.update_time)
    if item.create_time:
        db_query = db_query.filter(models.Human.create_time <= item.create_time)
        db_query = db_query.filter(models.Human.create_time >= item.create_time)
    return db_query.order_by(models.Human.id).all()


def delete_human(db: Session, item_id: int):
    db.query(models.Human).filter(models.Human.id == item_id).delete()
    db.commit()
    return True
