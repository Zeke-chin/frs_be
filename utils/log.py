# coding=utf-8
# Powered by SoaringNova Technology Company
import sys

import logging
import datetime
from pathlib import Path


def format_print():
    class GeneralWriter:
        def __init__(self, *writers):
            self.writers = writers

        def write(self, buf):
            now = datetime.datetime.now()
            ts = '{},{}'.format(now.strftime('%Y-%m-%d %H:%M:%S'), '%03d' % (now.microsecond // 1000))
            for w in self.writers:
                for line in buf.rstrip().splitlines():
                    msg = line.rstrip()
                    if len(msg):
                        w.write('\033[1;32;1m{}| {}\033[0m\n'.format(ts, msg))

        def flush(self):
            pass

    sys.stdout = GeneralWriter(sys.stdout)
    sys.stderr = GeneralWriter(sys.stdout)


# 设置日志文件的名称和位置
def log_init():
    root = Path(__file__).parent.parent / "logs"
    if not root.exists():
        root.mkdir()
    log_file = str(root / f"log_{str(datetime.datetime.now().date())}.log")
    # print(str(root/log_file))
    logging.basicConfig(filename=log_file, level=logging.INFO,
                        format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S')

    logging.info(f'{datetime.datetime.now()} 项目启动')
    return logging


from loguru import logger
import datetime
from pathlib import Path


def lr_init():
    root = Path(__file__).parent.parent / "logs"
    if not root.exists():
        root.mkdir()

    # 添加时间戳到日志文件名
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = str(root / f"log_{timestamp}.log")

    # 自定义日志格式
    log_format = "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level: <8} | {message}"

    logger.add(log_file, rotation="1 MB", format=log_format)
    logger.info(f'{datetime.datetime.now()} 项目启动')
    return logger
