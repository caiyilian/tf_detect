"""
这个程序用于将图片显示到lcd屏幕上
"""
from utils import LCD_2inch4
from cv2 import cvtColor,COLOR_BGR2RGB
from PIL import Image, ImageFilter
disp = LCD_2inch4.LCD_2inch4()
disp.Init()
disp.clear()


def show_lcd(frame):
    image = Image.fromarray(cvtColor(frame, COLOR_BGR2RGB))
    image = image.resize((320, 240), Image.ANTIALIAS)
    image = image.filter(ImageFilter.SHARPEN)
    disp.ShowImage(image)

if __name__ == '__main__':
    import time
    from cv2 import imread
    for i in range(30):
        img = imread(f"../datasets/0/{i}.jpg")    
        time.sleep(0.3)
        show_lcd(img)
