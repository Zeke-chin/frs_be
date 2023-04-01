import time
from fastapi_pagination import paginate, Params
from fastapi import FastAPI, WebSocket, Depends
from sqlalchemy.orm import Session

from app import schemas, get_db, crud
from utils import web_try, timeit
from fastapi import APIRouter
from app.common.validation import *

router_user = APIRouter(prefix="/user", tags=["user-用户管理"], )


@router_user.post("/", summary="用户创建")
@web_try()
@timeit
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.user.create_user(db, user)


@router_user.delete("/{user_id}", summary="用户删除")
@web_try()
@timeit
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.user.delete_user(db, user_id)


@router_user.put("/{user_id}", summary="用户更新")
@web_try()
@timeit
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db), ):
    return crud.user.update_user(db, user_id, user)


@router_user.get("/get", summary="用户列表")
@web_try()
@timeit
def get_users(get_item: schemas.UserGet = Depends(), params: Params = Depends(), db: Session = Depends(get_db), ):
    return paginate(crud.user.get_users(db, get_item), params)
