from pathlib import Path

from compre_face import draw_all
from utils.image import np2bytes
from .file import upload_file
from configs.settings import config
import cv2
from compreface.service import VerificationService
from compre_face.cf_core import compre_face

VERIFICATION_TOKEN = config.get("COMPREFACE", "VERIFICATION_TOKEN")

cf_verification: VerificationService = compre_face.init_face_verification(VERIFICATION_TOKEN)


def verify(img_source, img_target):
    """
    人脸对比
    :param img_source: 原图
    :param img_target: 目标图
    :return:
    """
    root = Path(__file__).parent.parent.parent / "static" / "files"
    img_source_path = str(root / img_source)
    img_target_path = str(root / img_target)
    res = cf_verification.verify(img_source_path, img_target_path)
    source_res = res['result'][0]['source_image_face']
    target_res = res['result'][0]['face_matches'][0]
    confidence_coefficient = target_res['similarity']
    color_code = 3 if confidence_coefficient > 0.8 else 1
    source_path = upload_file(np2bytes(draw_all(cv2.imread(img_source_path), source_res, color_code)))
    target_path = upload_file(np2bytes(draw_all(cv2.imread(img_target_path), target_res, color_code)))
    return {
        "source_path": source_path,
        "target_path": target_path,
        "confidence_coefficient": confidence_coefficient
    }
