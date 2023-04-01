def get_head_pose(res):
    pitch, roll, yaw = res['pitch'], res['roll'], res['yaw']
    pose = ""

    if pitch is None or roll is None or yaw is None:
        # return "头部姿势信息缺失"
        return "Head pose information is missing"

    if pitch > 19:
        # pose += "昂头 "
        pose += "up "
    elif pitch < 5:
        # pose += "低头 "
        pose += "down "
    else:
        # pose += "水平 "
        pose += "horizontal "

    # if roll > 10:
    #     # pose += "右倾 "
    #     pose += "right "
    # elif roll < -10:
    #     # pose += "左倾 "
    #     pose += "left "
    # else:
    #     # pose += "正面 "
    #     pose += "front "

    if yaw > 6:
        # pose += "左摇头"
        pose += "left"
    elif yaw < -16:
        # pose += "右摇头"
        pose += "right"
    else:
        # pose += "正对"
        pose += "front"
    return f"{pose}"
