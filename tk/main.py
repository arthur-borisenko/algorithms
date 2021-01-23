from screen_saver_widget import ScreenSaverWidget

# from threading import Thread
sleepInterval = 0.1
window_size = 500


def start():
    screen_saver = ScreenSaverWidget(window_size, sleepInterval)
    screen_saver.start()
start()
# threads=[]
# for i in range(10):
#    thread1 = Thread(target=start)
#    thread1.start()
#    threads.append(thread1)
# for thread in threads:
#    thread.join()
