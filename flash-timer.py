import keyboard
import time
import winsound
import threading

wait_time = 10  # 待機秒数
N = 0  # スペースキーのカウント変数

def on_space_pressed(event):
    global N
    if event.name == 'space':
        N += 1
        if N == 2:
            print("Space key pressed twice. Resetting timer.")
            time.sleep(wait_time)
            print(f"{wait_time} seconds passed. Playing sound.")
            winsound.Beep(300, 100)  # 300 Hz frequency for 100 milliseconds
            N = 0

def main():
    keyboard.on_press(on_space_pressed)
    print("Press ESC to stop.")
    keyboard.wait('esc')

if __name__ == "__main__":
    # スレッドを使ってバックグラウンドで実行
    thread = threading.Thread(target=main)
    thread.start()
