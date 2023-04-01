import time
from fastapi_pagination import paginate, Params
from fastapi import FastAPI, WebSocket, Depends
from starlette.responses import StreamingResponse
from app import schemas, get_db, crud
from utils import web_try, timeit
from fastapi import APIRouter
from app.common.validation import *

router_video = APIRouter(prefix="/video", tags=["video-返回视频流"], )


@router_video.get("/", summary="返回视频流")
async def video_feed():
    return StreamingResponse(crud.generate_video(), media_type="multipart/x-mixed-replace;boundary=frame")

@router_video.get("/screenshot", summary="返回截图")
@web_try()
@timeit
def screenshot():
    return crud.screenshot()

