


def my_decorator(func):
    def wrapper():
        print("before functions run ")
        func()
        print("after funtions run")
    return wrapper
    

@my_decorator
def greet():
    print("hello from rajasthan ")

greet()


# print(greet.__name__)
