from compreface import CompreFace
from configs.settings import config


# 初始化模型对象
HOST = config.get("COMPREFACE", "HOST")
PORT = config.get("COMPREFACE", "PORT")
compre_face: CompreFace = CompreFace(HOST,  # 服务器地址
                                     PORT,  # 服务器端口
                                     {"limit": 1,  # 要识别的图像上的最大人脸数。它首先识别最大的面孔。值为 0 表示没有限制
                                      "det_prob_threshold": 0.8,  # 检测阈值
                                      "prediction_count": 1,  # 识别结果数量
                                      "face_plugins": "age,gender,pose,landmarks,mask",  # 人脸识别插件
                                      "status": False})  # 系统信息
print("算法初始化完成")
