from concurrent.futures import thread
import threading
import time

# source: https://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread/49877671#49877671
# main discussion that shows a possible solution: https://github.com/miguelgrinberg/Flask-SocketIO/issues/1395


class SmartThread(threading.Thread):
    def __init__(self, sleep_interval=1, thread_id=''):
        super().__init__()
        self._kill_event = threading.Event()
        self._sleep_interval = sleep_interval
        self._thread_id = thread_id

    def run(self):
        ok = True
        idx = 1
        while True:
            print(f'Operation {idx}')

            # If no kill signal is set, sleep for the interval,
            # If kill signal comes in while sleeping, immediately
            #  wake up and handle
            is_killed = self._kill_event.wait(self._sleep_interval)
            if is_killed:
                ok = False
                break
            idx = idx + 1

        print(f"Stopping thread -> {self._thread_id}")

    def kill(self):
        self._kill_event.set()


def main():
    test_thread = SmartThread(sleep_interval=1, thread_id='thd01')
    test_thread.start()

    # this is inside the main function
    # outside the smart thread class
    time.sleep(3)

    # kill the background task executed by the smart thread
    test_thread.kill()


if __name__ == '__main__':
    main()
