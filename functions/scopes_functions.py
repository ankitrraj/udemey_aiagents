#  scopes

#  glloblac scope

hey = "how are you"
# there is a global varaible and its is in global
def check_the_global_scope():
     global hey 
     hey = 78
     print(hey)
    #   this change reference not copy to ensure that
    
check_the_global_scope()
# you print the global scope in lower scope but when you change use 'global' keyword
#  local scope
def local_scope():
    my_name = "ankit"
    print("localy my name is ",my_name)

local_scope()
my_name = "ankit rajoria"

print("golbaly my name is ",my_name)




# enclosing scope
def enscoping_scope():
    my_name = "ankit"
    def another_name():
        my_name = "AR"
        print(f"my not locally but another shortucut name is {my_name}")
    another_name()
    print("localy my name is ",my_name)

enscoping_scope()

#  built in


