def my_decorator(func):
    def wrapper():
        print("Step - 1")
        func()
        print("Step - 3")
    return wrapper


def repeat(func):
    def wrapper():
        for i in range(3):
            print("iter", i, ": ", end="")
            func()
    return wrapper
 

####################################
@my_decorator
@repeat
def start_steps():
    print("Step - 2")
 
 
start_steps()