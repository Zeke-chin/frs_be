from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from app.schemas import LogerLine

def get_logs():
    log_file = get_latest_file()
    with log_file.open(mode='r', encoding='utf-8') as file:
        content = [log_s2L(line.strip()) for line in file]
    return content


def get_latest_file():
    folder = Path(__file__).parent.parent.parent / 'logs'
    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        print("No files found in the folder.")
        return None

    return max(files, key=lambda x: x.stat().st_ctime)

def log_s2L(log_string: str):
    date_str = log_string.split(' | ', maxsplit=3)[0]
    level = log_string.split(' | ', maxsplit=3)[1].replace(' ', '')
    message = log_string.split(' | ', maxsplit=3)[2].split(' ')[-1]
    date_obj = datetime.fromisoformat(date_str)
    timestamp = int(date_obj.timestamp())
    return LogerLine(date=timestamp, level=level, message=message)
