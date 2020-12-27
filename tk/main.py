from tk.screen_saver_widget import ScreenSaverWidget
from threading import Thread

sleepInterval = 0.1
window_size = 500


def start():
    screen_saver = ScreenSaverWidget(window_size, sleepInterval)
    screen_saver.start()

for i in range(1):
    thread1 = Thread(target=start)
    thread1.start()