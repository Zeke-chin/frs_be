import time
from fastapi_pagination import paginate, Params
from fastapi import FastAPI, WebSocket, Depends
from sqlalchemy.orm import Session

from app import schemas, get_db, crud
from utils import web_try, timeit
from fastapi import APIRouter
from app.common.validation import *

router_user = APIRouter(prefix="/wx", tags=["user-用户管理"], )


# @app.websocket("/video_status")
# async def websocket_endpoint(websocket: WebSocket):
#     global status_code
#     await websocket.accept()
#     while True:
#         await websocket.send_text(f"Status code: {status_code}")
