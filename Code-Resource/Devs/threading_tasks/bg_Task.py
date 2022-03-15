import threads_main as local_thread

# do not work with smart thread
thread = local_thread.threading.Thread()
# create an event which will turn off a thread
stop_event_thread = local_thread.threading.Event()


def main():
    print(thread)
    print(stop_event_thread)


if __name__ == '__main__':
    main()
