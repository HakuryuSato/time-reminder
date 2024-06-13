import time
import winsound  # Windows用。macOS/Linuxなら`os`モジュールと`afplay`コマンドを使います。

def beep(duration):
    freq = 440  # 440Hzの音
    winsound.Beep(freq, duration)

intervals = {0: 1000, 15: 250, 30: 500, 45: 250}  # 分単位の時間とビープの長さ(ミリ秒)
while True:
    current_time = time.localtime()
    if current_time.tm_min in intervals and current_time.tm_sec == 0:
        beep(intervals[current_time.tm_min])
    time.sleep(1)