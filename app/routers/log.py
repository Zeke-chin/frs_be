from utils import web_try, timeit
from fastapi import APIRouter
from app.crud.log import get_logs

router_log = APIRouter(prefix="/log", tags=["log-日志管理"], )

# @router_log.get("/get", summary="日志列表")
# @web_try()
# @timeit
# def get_logs():
#

