from functools import wraps

def log_actitvity(fucn):

    @wraps(fucn)
    def wrapper(*args,**kwargs):
        print("hey how are you")
        fucn()
        print("hey there how much i not sacrifice")
        return fucn()
    return wrapper

@log_actitvity
def runthis(type):
    print(f"the type of {type} here it is")

runthis()