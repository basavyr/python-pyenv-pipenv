import threads_main as local_thread

# do not work with smart thread
thread = local_thread.threading.Thread()
# create an event which will turn off a thread
stop_event_thread = local_thread.threading.Event()


def check_for_event():
    return 1


def main():
    value = stop_event_thread.is_set()
    # do some calculations
    while value is False:
        print('thread is unset')
        print('...')
        local_thread.time.sleep(3)
        check_for_event()
    # try:
    #     assert value is True, 'The thread is not set!'
    # except AssertionError as err:
    #     print(err)


if __name__ == '__main__':
    main()
