import time
from threading import Thread
from compreface.service import RecognitionService
import cv2
from .draw import draw_all
from .pose import get_head_pose
import random
from utils.log import lr_init

logger = lr_init()

class ThreadedCamera:
    def __init__(self, url, cf_rec: RecognitionService):
        self.frame = cv2.imread("/compre_face/steven.jpeg")
        self.frame_draw_msg = cv2.imread("/compre_face/steven.jpeg")
        self.active = True
        self.current_instruction = None  # 当前指令
        self.status_code = 0  # 初始化状态码
        self.results = []
        self.capture = cv2.VideoCapture(url)  # self.capture 定义为一个cv2.VideoCapture()对象
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)  # 设置缓冲区大小

        # 初始化人脸识别服务
        self.recognition = cf_rec

        self.FPS = 1 / 30

        # 启动线程
        self.thread = Thread(target=self.show_frame, args=())
        self.thread.daemon = True
        self.thread.start()

    def show_frame(self):
        print("Started")
        # self.capture.isOpened()是一个bool值，如果视频流打开，返回True
        while self.capture.isOpened():
            (status, frame_raw) = self.capture.read()
            # 镜像反转
            self.frame = cv2.flip(frame_raw, 1)
            # self.frame = frame_raw

            # 对人脸处理
            if self.results and status:
                if self.status_code == 0:
                    self.generate_instruction()
                    self.status_code = 1
                results = self.results
                # print(self.)
                for result in results:
                    self.frame_draw_msg = draw_all(self.frame, result, self.status_code)
            else:
                self.frame_draw_msg = self.frame
                self.status_code = 0

    def is_active(self):
        return self.active

    def update(self):
        if not hasattr(self, 'frame'):
            return

        try:
            _, im_buf_arr = cv2.imencode(".jpg", self.frame, [cv2.IMWRITE_JPEG_QUALITY, 50])
            byte_im = im_buf_arr.tobytes()
            data = self.recognition.recognize(byte_im)
            self.results = data.get('result')
            if self.status_code == 1:
                self.check_liveness(get_head_pose(self.results[0]['pose']))
            print(self.status_code)
            print(self.current_instruction)
        except Exception as e:
            pass

    def check_liveness(self, pose):
        elapsed_time = time.time() - self.instruction_start_time

        if elapsed_time <= 8:
            if self.current_instruction in pose:
                self.status_code = 3
                self.current_instruction = None
                logger.info(f"{self.results[0]['subjects'][0]['subject']} 验证成功")
                return
        else:
            self.status_code = -1
            self.current_instruction = None
            logger.error(f"{self.results[0]['subjects'][0]['subject']} 验证失败")



    def generate_instruction(self):
        self.current_instruction = random.choice(['up', 'down', 'left', 'right'])
        self.instruction_start_time = time.time()