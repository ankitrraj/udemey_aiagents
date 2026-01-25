class Thatonebhess:
    def __init__(self,type_,size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"hey the {self.type} chai aur the value is {self.size}"



chaiorder  = Thatonebhess("garam",500)

print(chaiorder.summary())