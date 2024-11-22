import time

def time_decorator(func):
    def wrapper():
        start_time = time.time()
        print(start_time)
        func()
        end_time = time.time()
        print(end_time)
        print("Total time taken by Function :  ", end_time-start_time)
    return wrapper()


@time_decorator
def test_ui_1():
    print("Add a function, time taken by this function 1")
    time.sleep(2)

@time_decorator
def test_ui_2():
    print("Add a function, time taken by this function 2")
    time.sleep(5)