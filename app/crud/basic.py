from typing import Type
from sqlalchemy.orm import Session
import time
from sqlalchemy.orm.attributes import flag_modified

from app.models import BaseModel


def update_to_db(db: Session, item_id: int, update_item, model_cls: Type[BaseModel],extra: tuple = ()):
    db_item = db.query(model_cls).filter(model_cls.id == item_id).first()
    if not db_item:
        raise Exception('未找到该任务')
    update_dict = update_item.dict(exclude_unset=True)
    if len(extra) > 1:
        update_dict[extra[0]] = extra[1]
    for k, v in update_dict.items():
        if v is None:
            continue

        setattr(db_item, k, v)
        flag_modified(db_item, k)

    if hasattr(db_item, "update_time"):
        db_item.update_time = int(time.time())
    db.commit()
    db.flush()
    db.refresh(db_item)
    return db_item
