import time
import winsound  # Windows用 macOS/Linuxなら`os`モジュールと`afplay`コマンド
from plyer import notification # 通知用

def beep(duration):
    freq = 1000  # 音の周波数(Hz)
    winsound.Beep(freq, duration)
    
# 0: 1000 -> 0分に1000ミリ秒間鳴動
intervals = {0: 1500, 30: 1000}  # 30分ごと

def main():
    while True:
        current_time = time.localtime()
        current_minute, current_second = current_time.tm_min, current_time.tm_sec
        formatted_time = time.strftime("%m/%d/%H:%M", current_time)
        if current_second == 0 and current_minute in intervals:
            beep(intervals[current_minute])
            # notification.notify(title="time-reminder", message="its time") # 通知
            
            print("ビープしました:",formatted_time) # ビープ音
            time.sleep(60)  # 鳴動後1分間スリープ


        time.sleep(1)

if __name__ == "__main__":
    main()
