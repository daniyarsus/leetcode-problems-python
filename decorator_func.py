from typing import Callable
import time


def timer(seconds=None):
    def decorator(func: Callable) -> callable:
        def wrapper(*args, **kwargs) -> str:
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            elapsed_time = end_time - start_time
            if isinstance(seconds, int) and seconds > 0:
                print(f"{seconds} seconds")
            else:
                print(f"Elapsed time: {elapsed_time:.2f} seconds")
            return result
        return wrapper

    if callable(seconds):
        return decorator(seconds)
    else:
        return decorator


class Example:
    @timer(seconds=123213)
    def foo(self):
        time.sleep(2)


example = Example()
example.foo()


#@timer(seconds=123)
#def example():
#    time.sleep(0.2)
#
#
#example()
