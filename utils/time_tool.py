# coding=utf-8
# Powered by SoaringNova Technology Company
import errno
import os
import signal
import time
from collections import defaultdict
from functools import wraps
timer_counts = defaultdict(int)

class TimeoutError(Exception):
    pass


def timeout(seconds=10, error_message=os.strerror(errno.ETIME)):
    def decorator(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                signal.alarm(0)
            return result

        return wraps(func)(wrapper)

    return decorator


class TIMELIMIT:
    def __init__(self, limit_time=0):
        self.st = None
        self.et = None
        self.limit_time = limit_time

    def __enter__(self):
        self.st = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.et = time.time()
        dt = self.limit_time - (self.et - self.st) * 1000
        if dt > 0: time.sleep(float(dt) / 1000)


class TIMER:
    total_time = {}  # type: dict

    def __init__(self, tag='', enable_total=False, threshold_ms=0):
        self.st = None
        self.et = None
        self.tag = tag
        # self.tag = tag if not hasattr(g,'request_id') else '{} {}'.format(getattr(g,'request_id'),tag)

        self.thr = threshold_ms
        self.enable_total = enable_total
        if self.enable_total:
            if self.tag not in self.total_time.keys():
                self.total_time[self.tag] = []

    def __enter__(self):
        self.st = time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.et = time.time()
        dt = (self.et - self.st) * 1000
        if self.enable_total:
            self.total_time[self.tag].append(dt)

        if dt > self.thr:
            print ("{}: {}s".format(self.tag, round(dt / 1000, 4)))

    @staticmethod
    def output():
        for k, v in TIMER.total_time.items():
            print ('{} : {}s, avg{}s'.format(k, round(sum(v) / 1000, 2), round(sum(v) / len(v) / 1000, 2)))


def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        st = time.time()
        ret = func(*args, **kwargs)
        dt = time.time() - st
        endpoint = '{}.{}'.format(func.__module__, func.__name__)
        timer_counts[endpoint] += 1
        print('\n',"=============================================================")
        print ('{}[{}] finished, exec {}s'.format(endpoint,'%05d' % timer_counts[endpoint], round(dt, 5)))
        print("=============================================================",'\n')

        return ret

    return wrapper  # 返回

# def sxtimeit(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         endpoint = '{}.{}'.format(func.__module__, func.__name__)
#         setattr(g,'request_id','{}[{}]'.format(endpoint,'%05d' % timer_counts[endpoint]))
#         timer_counts[endpoint] += 0
#         st = time.time()
#         ret = func(*args, **kwargs)
#         dt = time.time() - st
#         print ('{} finished, exec {}s'.format(getattr(g,'request_id'), round(dt, 4)))
#         return ret
#
#     return wrapper  # 返回

def t2date(t):
    import datetime
    date = datetime.datetime.fromtimestamp(t)
    return '{}_{}_{}_{}:{}:{}'.format(date.year, date.month, date.day, date.hour, date.minute,date.second)


def day_begin(t):
    dsecs = 24 * 3600
    return (int(t) + 8 * 3600) // dsecs * dsecs - 8 * 3600


def hour_begin(t):
    hsecs = 3600
    return (int(t) + 8 * 3600) // hsecs * hsecs - 8 * 3600