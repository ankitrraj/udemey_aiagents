#  the self argument

class heypython:
    howmuch_money = 3400

    def get_money(self):
        return f"hey i will give you {self.howmuch_money} you take or not"


heyobj= heypython()

print(heyobj.get_money())
print(heypython.get_money(heyobj))  # its gives a error because heypython deosent have the context of him

heyobj1 = heypython()
# in that cases we have to provide the ocntext of the object so its runned
print(heypython.get_money(heyobj1))