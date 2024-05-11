"""
该程序用于获取和播放当前树莓派网络的内网IP，知道IP之后就可以远程连接树莓派
"""
from utils.play_sound2 import play
import socket

def get_local_ip():
    try:
        # 创建一个UDP套接字
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # 连接到一个外部的IP地址
        s.connect(("8.8.8.8", 80))
        # 获取本地套接字的IP地址和端口号
        local_ip = s.getsockname()[0]
        return local_ip.replace(".","_")
    except Exception as e:
        print("获取本地IP地址失败:", e)
        return None

def play_ip():
    ip = get_local_ip()
    if ip is None:
        return
    print("play")
    for num in ip:
        play(num)
    
    
if __name__ == "__main__":
    local_ip = get_local_ip()
    if local_ip:
        print("本地IP地址:", type(local_ip))
    else:
        print("无法获取本地IP地址")
