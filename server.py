from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from utils.sx_log import format_print
from app.routers.hello import *

format_print()
app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="人脸识别系统后台")

# CORS 跨源资源共享
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('server init finish:)!!!')
app.include_router(router_hello)

# Get 健康检查
@app.get("/ping", description="健康检查")
def ping():
    return "pong!!"
