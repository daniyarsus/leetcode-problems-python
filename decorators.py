import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print('Time: {:.3f}'.format(end - start))
        return result
    return wrapper



@timer
def example():
    time.sleep(0.2)


example()
