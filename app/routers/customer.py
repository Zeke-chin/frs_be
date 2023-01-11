from fastapi import APIRouter, Depends
from fastapi_pagination import paginate, Params
from sqlalchemy.orm import Session
from app.common.validation import *
from app import schemas, get_db, crud
from utils import web_try, sxtimeit

router_customer = APIRouter(
    prefix="/customer",
    tags=["customer-用户管理"],
)


@router_customer.get("/", summary="获取用户列表")
@web_try()
@sxtimeit
def get_customers(get_item: schemas.CustomerGet = Depends(), params: Params = Depends(), db: Session = Depends(get_db),
                  user=Depends(check_admin)):
    return paginate(crud.get_customers(db, get_item), params)
