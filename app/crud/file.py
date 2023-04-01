import io
import time
from datetime import datetime
from pathlib import Path
from typing import List
import uuid
from fastapi.responses import StreamingResponse
from app import models, schemas
from sqlalchemy.orm import Session
from app.crud.basic import update_to_db
from app.common.validation import *


def upload_file(file_byte):
    file_name = str(f'{uuid.uuid4()}.jpg')
    root_path = Path(__file__).parent.parent.parent / 'static' / 'files' / datetime.now().strftime('%Y%m%d')
    if not root_path.exists():
        root_path.mkdir(parents=True)
    file_path = root_path / file_name
    with open(file_path, 'wb') as f:
        f.write(file_byte)
    return str(file_path).split('files/')[-1]


def get_file(file_name: str):
    file_path = Path(__file__).parent.parent.parent / 'static' / 'files' / file_name
    print(file_path)
    return StreamingResponse(open(file_path, 'rb'), media_type='image/jpeg')
