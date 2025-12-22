# pure or impure 

def pure_chai(cups):
    return cups *10


# recurisive functions 

def hey_check(n):
    print(n)
    if n==0:
        return "hey that is correct "
    return hey_check(n-1)
print(hey_check(4))



#  lambdas

chai_types = ["light","strong","ginger","light"]

st = list(filter(lambda chai:chai!="light",chai_types))


print(st)