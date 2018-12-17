def run_only(time=1, message=None):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.count != time:
                wrapper.count += 1
                return func(*args, **kwargs)
            else:
                if message is not None:
                    print(message)
        wrapper.count = 0
        return wrapper
    return decorator


run_once = run_only(1)


def run_once_message(message=None):
    return run_only(1, message)

