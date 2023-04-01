from threading import Thread
from compreface.service import RecognitionService
import cv2
from .draw import draw_all


class ThreadedCamera:
    def __init__(self, url, cf_rec: RecognitionService):
        self.frame = cv2.imread("/compre_face/steven.jpeg")
        self.frame_draw_msg = cv2.imread("/compre_face/steven.jpeg")
        self.active = True
        self.results = []
        self.capture = cv2.VideoCapture(url)  # self.capture 定义为一个cv2.VideoCapture()对象
        self.capture.set(cv2.CAP_PROP_BUFFERSIZE, 2)  # 设置缓冲区大小

        # 初始化人脸识别服务
        self.recognition: cf_rec

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
                results = self.results
                print(results)
                for result in results:
                    self.frame_draw_msg = draw_all(self.frame, result)

            # cv2.imshow('CompreFace demo', self.frame)  # time.sleep(self.FPS)  #  # # 按下ESC键退出  # if cv2.waitKey(1) & 0xFF == 27:  #     self.capture.release()  #     cv2.destroyAllWindows()  #     self.active = False

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
        except Exception as e:
            pass


if __name__ == '__main__':
    # args = parseArguments()
    # threaded_camera = ThreadedCamera(args.api_key, args.host, args.port)
    threaded_camera = ThreadedCamera("baa6dd79-221f-468a-831b-0c2780377d3c", "http://192.168.192.86", "8000")
    while threaded_camera.is_active():
        threaded_camera.update()
