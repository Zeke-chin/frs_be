import time
from fastapi_pagination import paginate, Params
from fastapi import FastAPI, WebSocket, Depends
from starlette.responses import StreamingResponse
from app import schemas, get_db, crud
from utils import web_try, timeit
from fastapi import APIRouter
from app.common.validation import *
from fastapi import FastAPI, WebSocket
from fastapi.responses import StreamingResponse
import asyncio
import cv2

router_video = APIRouter(prefix="/video", tags=["video-返回视频流"], )


@router_video.get("/", summary="返回视频流")
async def video_feed():
    return StreamingResponse(crud.generate_video(), media_type="multipart/x-mixed-replace;boundary=frame")

@router_video.get("/screenshot", summary="返回截图")
@web_try()
@timeit
def screenshot():
    return crud.screenshot()

@router_video.get("/status", summary="返回状态")
@web_try()
@timeit
def status():
    return crud.get_status()

# @router_video.websocket("/ws")
# async def websocket_video(websocket: WebSocket):
#     await websocket.accept()
#     async for frame_data in crud.generate_video_wx():
#         print("Sending frame")
#         await websocket.send_bytes(frame_data)
