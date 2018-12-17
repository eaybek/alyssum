counter_list = []


class Counter(object):
    counter = 0

    def __init__(self, time, func):
        self.time = time
        self.func = func

    def count(self):
        if self.counter != self.time:
            self.counter += 1
            return True
        else:
            return False


def search_list(func):
    for i in counter_list:
        if i.func == func:
            return i
    return None


def get_counter(func, time):
    counter = search_list(func)
    if counter is None:
        counter = Counter(time, func)
        counter_list.append(counter)
    return counter


def run_only(time=1, message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            c = get_counter(func.__name__, time)
            if c.count():
                return func(*args, **kwargs)
            else:
                if message is not None:
                    print(message)
        return wrapper
    return decorator


run_once = run_only(1)


def run_once_message(message=None):
    return run_only(1, message)

