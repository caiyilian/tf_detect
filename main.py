"""
这个程序是主程序
"""
import cv2
from utils.play_sound2 import play
from utils.tf_cls import MinesClassifier
from utils.lcd_util import show_lcd
from utils.read_rpi import get_io_state
cap = cv2.VideoCapture(0)
mine_classifier = MinesClassifier(paddle_model="./models/MV2.nb")


def get_img():
    """
    获取一帧摄像头图像
    :return:
    """
    while True:
        success,img = cap.read()
        if success is False:
            continue
        break
    return img

def is_broken_continue():
    # 是否连续三张图像都是塌方，是的话就不是噪声，相当于滤波
    broken_num = 0
    for i in range(3):
        img = get_img()
        result = mine_classifier.recognize_img(img)
        if result != 0:
            break
        broken_num += 1
    if broken_num < 3:
        # 如果不能连续三张都是塌方，那就认为没有塌方，是噪声
        return False
    return True

# 让你调节摄像头位置，对准道路模型，如果你调节好了，就让IO0置为高电平
play("wait")
while True:
    img = get_img()
    show_lcd(img)
    if get_io_state() == 1:
        print("begin")
        break



# 开始进入实时监控道路是否塌方的程序
play("begin")
# 决定开启和关闭识别，如果关闭识别，就仅仅把图像显示到LCD屏幕
use_model = True
# 这个是为了防止重复报警，只要你检测到塌方，报警一次后，将这个赋值为True，那么就不会响应连续的塌方导致lcd图像显示卡顿
is_broken = False
while True:
    # 获取图像
    img = get_img()
    show_lcd(img)
    if use_model is True:
        # 识别图像,result=1的话就是未塌方，result=0就是塌方
        result = mine_classifier.recognize_img(img)

        # 疑似塌方
        if result == 0 and is_broken is False:
            # 先检测接下来的几张图片是否也都是塌方，如果是的话，那就是真的塌方，不然可能就是噪声干扰
            if is_broken_continue() is False:
                continue
            is_broken = True
            play("music")
            print("broken")
        if result == 1:
            is_broken = False
    # 如果现在是开启识别状态，并且IO0是低电平，那就转为停止识别状态
    if use_model is True and get_io_state() == 0:
        use_model = False
        play("stop")
    # 如果现在是停止识别状态，并且IO0是高电平，那就转为开启识别状态
    if use_model is False and get_io_state() == 1:
        use_model = True
        play("begin")
    # 如果IO1是高电平，那就退出系统
    if get_io_state(True) == 1:
        play("exit")
        exit()
    
