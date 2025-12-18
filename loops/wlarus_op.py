# walrus opertor :=  is this help to save a line in your code base 


# your_num = 45

# if(divide := your_num % 4):
#     print(f"remiander is {divide} ")

# my_list  = ["ankit","rohit","ankesh","sher"]
my_list  = ["ankit","rohit","ankesh","sher"]

# print(type(my_list))

if (user_input := input("give me a name::::")) in my_list:
    print(f"the name is {user_input}  is correct")
else:
    print(f"your name is wrong {user_input}")

