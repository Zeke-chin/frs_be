import numpy as np
import cv2
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt
from .pose import get_head_pose

# color = (0, 255, 0)
en2ch = {"female": "女", "male": "男", "without_mask": "无口罩", "with_mask": "有口罩",
         "mask_weared_incorrect": "口罩佩戴不正确", "mask_weared_correctly": "口罩佩戴正确"}
global color
color = (0, 255, 255)

def draw_all(image, result, status_code):
    global color
    if status_code == 1: # 黄色
        color = (0, 255, 255)
    elif status_code == 3: # 绿色
        color = (0, 255, 0)
    elif status_code == -1: # 红色
        color = (0, 0, 255)
    draw_pipline = []
    if result["box"]:
        image_ = draw_box(image, result)  # bv = box_val(result)
    if result["subjects"]:
        draw_pipline.append(text_subject(result))
    if result["age"]:
        draw_pipline.append(text_age(result))
    if result["gender"]:
        draw_pipline.append(text_gender(result))
    if result["mask"]:
        draw_pipline.append(text_mask(result))
    if result["pose"]:
        draw_pipline.append(text_pose(result))
    return cv_put_text_pipline(image_, draw_pipline)


def cv_put_text_pipline(img, pipline, text_size=1, text_weight=1):
    global color
    text_color = color
    for text, position in pipline:
        cv2.putText(img, text, position, cv2.FONT_HERSHEY_COMPLEX, text_size, text_color, text_weight)
    return img


def cv2AddChineseText(img, pipline, textSize=30):
    global color
    textColor = color
    # def cv2AddChineseText(img, pipline,box, textColor=color, textSize=30):
    image_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    # 创建一个可以在给定图像上绘图的对象
    draw = ImageDraw.Draw(image_pil)
    # 字体的格式
    font = ImageFont.truetype('/Users/zeke/work/frs_be/font/simsun.ttc', textSize)
    # 绘制文本
    for text, position in pipline:
        draw.text(position, text, font=font, fill=textColor)
    # draw.rectangle(box, outline=color)
    return cv2.cvtColor(np.array(image_pil),
                        cv2.COLOR_RGB2BGR)  # return cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, 1, textColor, 2, cv2.LINE_AA)


def draw_box(image, result):
    global color
    box_dict = result['box']
    l, t, r, b = box_dict['x_min'], box_dict['y_min'], box_dict['x_max'], box_dict['y_max']
    cv2.rectangle(img=image, pt1=(l, t), pt2=(r, b), color=color, thickness=2)
    return image


def box_val(result):
    box_dict = result['box']
    return [box_dict['x_min'], box_dict['y_min'], box_dict['x_max'], box_dict['y_max']]


def text_subject(result):
    subject_dict = result['subjects'][0]
    return f"name: {subject_dict['subject']}", (result['box']['x_max'] + 5, result['box']['y_min'] + 15)


def text_age(result):
    age_dict = result['age']
    return f"age: {age_dict['low']}-{age_dict['high']}", (result['box']['x_max'] + 5, result['box']['y_min'] + 45)


def text_gender(result):
    gender_dict = result['gender']
    return f"gender: {gender_dict['value']}", (result['box']['x_max'] + 5, result['box']['y_min'] + 75)


def text_mask(result):
    mask_dict = result['mask']
    return f"mask: {mask_dict['value']}", (result['box']['x_max'] + 5, result['box']['y_min'] + 105)


def text_pose(result):
    pose_dict = result['pose']
    return f"pose: {get_head_pose(pose_dict)}", (result['box']['x_max'] + 5, result['box']['y_min'] + 135)

# if __name__ == '__main__':
