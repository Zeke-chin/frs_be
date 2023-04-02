import asyncio

from .file import upload_file
from configs.settings import config
import cv2
from compreface import CompreFace
from compreface.service import RecognitionService
from typing import Generator
from compre_face import *
from utils.image import *
from compre_face.cf_core import compre_face

RECOGNITION_TOKEN = config.get("COMPREFACE", "RECOGNITION_TOKEN")
VIDEO_URL = 0 if config.get("COMPREFACE", "VIDEO_URL") == "0" else config.get("COMPREFACE", "VIDEO_URL")

# 初始化识别模型对象

cf_recognition: RecognitionService = compre_face.init_face_recognition(RECOGNITION_TOKEN)

# 初始化 - 算法
threaded_camera = ThreadedCamera(VIDEO_URL, cf_recognition)


async def generate_video() -> Generator[bytes, None, None]:
    while threaded_camera.is_active():
        # 获取处理后的帧
        threaded_camera.update()
        processed_frame = threaded_camera.frame_draw_msg

        # 将处理后的帧发送到客户端
        try:
            ret, buffer = cv2.imencode('.jpg', processed_frame)
            # ret, buffer = cv2.imencode('.jpg', processed_frame,[cv2.IMWRITE_JPEG_QUALITY, 80])
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        except Exception as e:
            pass
        await asyncio.sleep(threaded_camera.FPS * 1.5)

# async def generate_video_wx() -> Generator[bytes, None, None]:
#     while threaded_camera.is_active():
#         # 获取处理后的帧
#         threaded_camera.update()
#         processed_frame = threaded_camera.frame_draw_msg
#
#         # 将处理后的帧发送到客户端
#         try:
#             ret, buffer = cv2.imencode('.jpg', processed_frame)
#             # ret, buffer = cv2.imencode('.jpg', processed_frame, [cv2.IMWRITE_JPEG_QUALITY, 80])
#             frame = buffer.tobytes()
#             yield frame
#         except Exception as e:
#             pass
#         await asyncio.sleep(threaded_camera.FPS)

# 截图
def screenshot():
    threaded_camera.update()
    screenshot = np2bytes(threaded_camera.frame)
    return upload_file(screenshot)

def get_status():
    return threaded_camera.status_code

