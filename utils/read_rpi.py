"""
这个程序用于读取树莓派的IO口的电平情况
"""
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
# 7月份钣金小车版本对应扩展板的 io_BCM字典
IO2GPIO = {0: 16, 1: 12, 2: 25,
           3: 24, 4: 22, 5: 23,
           6: 27, 7: 17, 8: 4}


gpio_num = IO2GPIO[0]
GPIO.setup(gpio_num, GPIO.OUT)

gpio_num1 = IO2GPIO[1]
GPIO.setup(gpio_num1, GPIO.OUT)
def get_io_state(check_close=False):
    if check_close:
        return GPIO.input(gpio_num1)
    return GPIO.input(gpio_num)


if __name__ == "__main__":
    import time
    start = time.time()
    print(get_io_state())
    print((time.time()-start),"ms")
