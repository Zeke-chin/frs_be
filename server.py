from fastapi import FastAPI  # 导入FastAPI
from fastapi.middleware.cors import CORSMiddleware  # 导入cors解决跨域问题
from utils.sx_log import format_print  # 导入utils.sx_log
# 导入hello路由
from app.routers.hello import *
from app.routers.human import *

format_print()
app = FastAPI(docs_url='/docs', redoc_url='/redoc', title="人脸识别系统后台")  # app的url

# CORS 跨源资源共享
app.add_middleware(  # 配置CORSMiddleware
    CORSMiddleware,
    allow_origins=["*"],  # 允许发出跨域请求的源列表
    allow_credentials=True,  # 跨域请求应该支持 cookie
    allow_methods=["*"],  # 允许跨域请求的 HTTP 方法列表
    allow_headers=["*"],  # 允许跨域请求携带的 HTTP Request Headers 列表
)

# 标识位 表示完成已经初始化
print('server init finish:)!!!')
# 引入hello路由
app.include_router(router_hello)
app.include_router(router_human)


# Get 健康检查
@app.get("/ping", description="健康检查")
def ping():
    return "pong!!"
