


def my_decorator(func):
    def wrapper():
        print("before functions run ")
        func()
        print("after funtions run")
    wrapper()

@my_decorator
def greet():
    print("hello from rajasthan ")



# print(greet.__name__)
