from fastapi import APIRouter, UploadFile, File
from utils import web_try, timeit
from app.crud import file


router_file = APIRouter(prefix="/file", tags=["file-文件管理"])


@router_file.post("", summary="上传文件")
@web_try()
@timeit
def upload_file(up_file: UploadFile = File(...)):
    return file.upload_file(up_file.file.read())


@router_file.get("/{file_name:path}", summary="获取文件")
@timeit
def get_file(file_name: str):
    return file.get_file(file_name)
