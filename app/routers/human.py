from fastapi import APIRouter, Depends#用户相关的路径操作与其余代码分开
from fastapi_pagination import paginate, Params#导入fastapi_pagination，用于将数据进行分页和提供分页参数
from sqlalchemy.orm import Session#导入orm

from app import schemas, get_db, crud#在app建包：创建模型，也就是接口传的一些参数；get_db函数；放置执行数据操作
from utils import web_try, sxtimeit#在utils设web_try, sxtimeit

router_human = APIRouter(
    prefix="/human",
    tags=["人像管理"],
)


@router_human.post("", summary="创建人像")
@web_try()
@sxtimeit
def human_create(item: schemas.HumanCreate, db: Session = Depends(get_db)):
    return crud.create_human(db=db, item=item)

@router_human.get("", summary="获取人像列表")
@web_try()
@sxtimeit
def human_get(params: Params = Depends(), db: Session = Depends(get_db)):
    return paginate(crud.get_human(db=db, item=schemas.HumanGet()), params)

@router_human.get("/{item_id}", summary="获取人像")
@web_try()
@sxtimeit
def human_get_once(item_id: int, db: Session = Depends(get_db)):
    return crud.get_human_once(db=db, item_id=item_id)

@router_human.put("/{item_id}", summary="更新人像")
@web_try()
@sxtimeit
def human_update(item_id: int, item: schemas.HumanUpdate, db: Session = Depends(get_db)):
    return crud.update_human(db=db, item_id=item_id, update_item=item)

@router_human.delete("/{item_id}", summary="删除人像")
@web_try()
@sxtimeit
def human_delete(item_id: int, db: Session = Depends(get_db)):
    return crud.delete_human(db=db, item_id=item_id)

