import threads_main as local_thread

# do not work with smart thread
thread = local_thread.threading.Thread()
# create an event which will turn off a thread
stop_event_thread = local_thread.threading.Event()


def check_for_event(event):
    if event.is_set() is True:
        return 1
    else:
        return 0


def create_stop_event(event):
    print('will set the thread')
    return event.set()


def main():
    # do some calculations
    print('thread is unset')
    while stop_event_thread.is_set() is False:
        print('...')
        local_thread.time.sleep(3)
        # if(check_for_event(stop_event_thread) == 0):
        #     pass
        # else:
        #     create_stop_event(stop_event_thread)
        create_stop_event(stop_event_thread)
        # try:
        #     assert value is True, 'The thread is not set!'
        # except AssertionError as err:
        #     print(err)
        print('finished the task execution')


if __name__ == '__main__':
    main()
