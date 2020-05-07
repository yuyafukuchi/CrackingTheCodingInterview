import time
import concurrent.futures

def func1():
    for i in range(10):
        print(f"process1: {i}")
        time.sleep(1)


def func2():
    for i in range(10):
        print(f"process2: {i}")
        time.sleep(1)


if __name__ == "__main__":
    # executor = concurrent.futures.ProcessPoolExecutor(max_workers=2)
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    executor.submit(func1)
    executor.submit(func2)