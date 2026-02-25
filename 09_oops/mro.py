class A:
    sher =  "hello bro and sher"
class B(A):
    sher = "bro kaise hai sher"
class C(A):
    sher = "bro mohterboard"

class D(B,C):
    pass

another = D()
print(another.sher)