from .re_face import cf_recognition
from pathlib import Path

cf_storekeeper = cf_recognition.get_face_collection()
cf_subjects = cf_recognition.get_subjects()

def face_add(face_path: str, face_name: str):
    # sourcery skip: remove-unnecessary-cast
    ab_path = Path(__file__).parent.parent.parent / 'static' / 'files' / face_path
    try:
        res = cf_storekeeper.add(str(ab_path), face_name)
        print("添加",res)
        ab_path = ab_path.rename(Path(ab_path).parent / f"{res['image_id']}.jpg")
        return f"{str(ab_path).split('files/')[-1]}"
    except Exception as e:
        raise e

def subject_del(subject_name: str):
    try:
        res = cf_subjects.delete(subject_name)
        print('del', res)
        return True
    except Exception as e:
        raise e
