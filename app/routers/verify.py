from fastapi import APIRouter, UploadFile, File
from utils import web_try, timeit
from app import schemas, get_db, crud


router_verify = APIRouter(prefix="/verify", tags=["verify-人脸对比"])

@router_verify.post("", summary="人脸对比")
@web_try()
@timeit
def verify_face(images: schemas.VerifyPost):
    return crud.verify(images.source_path, images.target_path)

