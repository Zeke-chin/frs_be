from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.staticfiles import StaticFiles
import cv2
from app.models.database import Base, engine
from utils.log import format_print
from app.routers.user import router_user
from app.routers.cf import router_video
from app.routers.file import router_file
from app.routers.verify import router_verify
from app.routers.log import router_log

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

print('server init finish:)!!!')
app.include_router(router_user)
app.include_router(router_video)
app.include_router(router_file)
app.include_router(router_video)
app.include_router(router_verify)
app.include_router(router_log)


async def ping():
    return "pong"
