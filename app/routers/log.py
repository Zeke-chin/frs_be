from fastapi_pagination import paginate, Params
from fastapi import FastAPI, WebSocket, Depends

from utils import web_try, timeit
from fastapi import APIRouter
from app import schemas, get_db, crud

router_log = APIRouter(prefix="/log", tags=["log-日志管理"], )

@router_log.get("/get", summary="日志列表")
@web_try()
@timeit
def get_logs(params: Params = Depends()):
    return paginate(crud.log.get_logs(), params)



