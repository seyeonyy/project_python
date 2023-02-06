import time
from plyer import notification

while True:
    notification.notify(
        title = '배터리 부족',
        message = '새 장치를 컴퓨터에 연결해야 합니다.',
        app_icon = r"C:\Users\seyeon\Downloads\batterylow.ico",
        timeout = 60
    )
    time.sleep(60*60*8)
