from fastapi import APIRouter, Depends#用户相关的路径操作与其余代码分开
from fastapi_pagination import paginate, Params#导入fastapi_pagination，用于将数据进行分页和提供分页参数
from sqlalchemy.orm import Session#导入orm

from app import schemas, get_db, crud#在app建包：创建模型，也就是接口传的一些参数；get_db函数；放置执行数据操作
from utils import web_try, sxtimeit#在utils设web_try, sxtimeit

router_hello = APIRouter(
    prefix="/hello",#路由的前缀
    tags=["hello-测试"],#将应用于特定路径操作的内容
)


@router_hello.post("/test", summary="hello word post接口")
@web_try()
@sxtimeit
def add_admin():
    return "hello word！"

