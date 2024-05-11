"""
这个程序用于播放mp3音频文件
"""
import vlc
import os

def get_media_path():
    utils_path = os.path.dirname(__file__)
    tf_detect_path = os.path.dirname(utils_path)
    media_path = os.path.join(tf_detect_path,"media")
    return media_path

media_path = get_media_path()



def play(name):
    # 创建VLC播放器实例
    player = vlc.MediaPlayer()
    # 设置音量为80（可以根据需要调整）
    player.audio_set_volume(120)
    # 加载音频文件
    media = vlc.Media(os.path.join(media_path,f"{name}.mp3"))

    # 将媒体加载到播放器中
    player.set_media(media)
    # 播放音频文件
    player.play()

    # 等待音频播放完成
    while True:
        # 检查是否仍在播放
        if player.get_state() == vlc.State.Ended:
            break
    # 释放资源
    player.release()
if __name__ == '__main__':
    import time
    play()

