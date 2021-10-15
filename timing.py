import time
def calculate_time(func):
    # wrapper function that calls the parent function inside
    def wrap_time():
        before=time.time()
        func()
        #Calculate via subtracting initial and final time
        print("Total time", time.time()-before)
    return wrap_time


