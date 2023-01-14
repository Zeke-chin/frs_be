# Dependency
def get_db():
    try:
        from app.models.database import SessionLocal#从app.models.database中导入SessionLocal。
        db = SessionLocal()
        yield db
    finally:
        db.close()## 用get_db()来用于获取sessionLocal以及及时关闭连接

async def get_page(#定义页数
    page: int = 1, size: int = 10#当前为第一页，每页的记录数,默认为10。
):
    return {"page": page, "size": size}

def page_help(data, page: int, size: int, total: int = None):
    if total is None:
        total = len(data)
        data = data[(page - 1) * size:page * size]
    return {"item":data, "extra_data": {"page":page, "size":size, "total":total}}

