from dataclasses import dataclass
from pathlib import Path

def get_logs():
    log_file = get_latest_file()
    with log_file.open(mode='r', encoding='utf-8') as file:
        content = [line.strip() for line in file]
    return content


def get_latest_file():
    folder = Path(__file__).parent.parent.parent / 'logs'
    files = [f for f in folder.iterdir() if f.is_file()]

    if not files:
        print("No files found in the folder.")
        return None

    return max(files, key=lambda x: x.stat().st_ctime)

