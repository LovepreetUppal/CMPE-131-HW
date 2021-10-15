import time
def calculate_time(func):
    def wrap_time():
        before=time.time()
        func()
        print("Total time in seconds:", time.time()-before)
    return wrap_time


