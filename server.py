from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles

from app.models.database import Base, engine
from utils.log import format_print
from app.routers.user import router_user
from app.routers.core import router_video
from app.routers.file import router_file

# 初始化 - FastAPI
format_print()
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="人脸识别服务后台")
origins = ["*"]
# CORS 跨源资源共享
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 初始化模型对象


print('server init finish:)!!!')
app.include_router(router_user)
app.include_router(router_video)
app.include_router(router_file)

async def ping():
    return "pong"
