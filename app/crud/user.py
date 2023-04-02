import time
from typing import List
from app import models, schemas
from sqlalchemy.orm import Session
from app.crud.basic import update_to_db
from app.crud.re_face import cf_recognition
from app.crud.cf_storekeeper import face_add, subject_del


def create_user(db: Session, item: schemas.UserCreate):
    # sourcery skip: use-named-expression
    # 重复用户名检查
    res: models.User = db.query(models.User).filter(models.User.name == item.name).first()
    if res:
        raise Exception(f"用户 {item.name} 已存在")
    # 重复邮箱检查
    res: models.User = db.query(models.User).filter(models.User.email == item.email).first()
    if res:
        raise Exception(f"邮箱 {item.email} 已存在")
    # 添加到人脸库
    if item.name and item.head_img:
        item.head_img = face_add(item.head_img, item.name)
    # 创建
    db_item = models.User(**item.dict(), **{"create_time": int(time.time()),
                                            "update_time": int(time.time()),
                                            "last_auth_time": int(time.time())})
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


def update_user(db: Session, item_id: int, update_item: schemas.UserUpdate):
    return update_to_db(update_item=update_item, item_id=item_id, db=db, model_cls=models.User)


def get_users(db: Session, item: schemas.UserGet):
    db_query = db.query(models.User)
    if item.id:
        db_query = db_query.filter(models.User.id == item.id)
    if item.name:
        db_query = db_query.filter(models.User.name == item.name)
    if item.email:
        db_query = db_query.filter(models.User.email == item.email)
    if item.create_time is not None and item.create_time != 0:
        db_query = db_query.filter(models.User.create_time <= item.create_time + 86400)
        db_query = db_query.filter(models.User.create_time >= item.create_time)
    if item.update_time is not None and item.update_time != 0:
        db_query = db_query.filter(models.User.update_time <= item.update_time + 86400)
        db_query = db_query.filter(models.User.update_time >= item.update_time)
    if item.last_auth_time is not None and item.last_auth_time != 0:
        db_query = db_query.filter(models.User.last_auth_time <= item.last_auth_time + 86400)
        db_query = db_query.filter(models.User.last_auth_time >= item.last_auth_time)
    return db_query.all()


def delete_user(db: Session, item_id: int):
    item = db.query(models.User).filter(models.User.id == item_id).first()
    subject_del(item.name)
    db.delete(item)
    db.commit()
