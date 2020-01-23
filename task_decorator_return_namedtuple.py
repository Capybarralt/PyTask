from collections import namedtuple

def return_namedtuple(*names):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if isinstance(result, tuple):
                Action = namedtuple('Action',(*names,))
                result = Action(*result)
            return result
        return wrapper
    return decorator
