"""
这个程序用于树莓派开机自启动，树莓派开机会自动运行run_program.sh，这个sh文件会自动在这个路径下面运行这个程序
来开机自启
顺带一提，open_jupyter.sh是开机自启动jupyter，再结合树莓派的ip地址，就可以远程用jupyter来访问树莓派，
方便调试开发
"""
import os
from utils.play_sound2 import play


os.chdir("/home/pi/Desktop/guangshe/tf_detect")

play("power_up")
os.system("python3 main.py")

    

