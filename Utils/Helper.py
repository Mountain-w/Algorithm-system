import time


def timer(func):
    def inner(*arg, **kwargs):
        start = time.time()
        result = func(*arg, **kwargs)
        print(time.time() - start)
        return result

    return inner
