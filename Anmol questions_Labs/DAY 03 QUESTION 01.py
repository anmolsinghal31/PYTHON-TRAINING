import time
from functools import wraps


def execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # PT. 1: Measures the execution time of a function
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start

        # PT. 2: Prints the function name and execution time
        print(f"Function {func.__name__} executed in {duration:.4f}s")

        return result

    return wrapper


@execution_time
def test_function():
    time.sleep(0.5)


test_function()
