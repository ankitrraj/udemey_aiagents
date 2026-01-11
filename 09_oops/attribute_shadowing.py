class hello:
    temp = 45
    weather = "monsoon"


print(hello.temp)

createobj = hello()

createobj.sher = "meow"

print(createobj.temp)

createobj.temp =56

print(createobj.temp)
print(createobj.sher)
del createobj.temp

print(createobj.temp)
del createobj.sher
print(createobj.sher)


# notes

#  the attribute shdowing says when a class dosent ahve a defalut property of somethings
# and you create after the class so its has a another object so when it has delte so its gives error
