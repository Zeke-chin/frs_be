from fastapi import APIRouter, Depends
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session

from app import schemas, get_db, crud
from utils import web_try, sxtimeit

router_hello = APIRouter(
    prefix="/hello",
    tags=["hello-测试"],
)


@router_hello.post("/test", summary="hello word post接口")
@web_try()
@sxtimeit
def add_admin():
    return "hello word！"

