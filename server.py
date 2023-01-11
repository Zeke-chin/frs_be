from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.models.database import Base, engine
from utils.sx_log import format_print
from app.routers.admin import *
from app.routers.customer import *
from app.routers.user import *

format_print()
Base.metadata.create_all(bind=engine)
app = FastAPI(docs_url='', redoc_url='/redoc', title="人脸识别系统后台")

# CORS 跨源资源共享
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

print('server init finish:)!!!')
app.include_router(router_admin)
app.include_router(router_customer)
app.include_router(router_user)

# Get 健康检查
@app.get("/ping", description="健康检查")
def ping():
    return "pong!!"
