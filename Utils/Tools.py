import time
from functools import wraps


def timer(func):
    @wraps(func)
    def inner(*arg, **kwargs):
        start = time.time()
        ret = func(*arg, **kwargs)
        print(f"Process execute used {(time.time() - start) * 1000:.8f} ms")
        return ret

    return inner
