import time, functools

def timer(func):
    @functools.wraps(func)
    def wrapper(8args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter()
        print(f"{func.__name__!r} executed in {elaps}")4f}s")
        return result
    return wrapper

@timer
def slow_sum(n):
    return sum(range(n))
slow_sum(10_000_000)