def run_only(time):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if wrapper.count != time:
                wrapper.count += 1
                return func(*args, **kwargs)
        wrapper.count = 0
        return wrapper
    return decorator
run_once = run_only(1)
