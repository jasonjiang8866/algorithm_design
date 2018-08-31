import functools

def decorator(func):
    @functools.wraps(func)#preserve information about the original function like __name__
    def wrapper_decorator(*args, **kwargs):
        # Do something before
        value = func(*args, **kwargs)
        # Do something after
        return value
    return wrapper_decorator
