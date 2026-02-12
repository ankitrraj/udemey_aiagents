class chai:
    def __init__(self,name_):
        self.name = name_

    def print_the(self):
        print(self.name)
        print("sher")
class mas(chai):
    chai_cls = chai

    def __init__(self):
        self.chai = self.chai_cls("reg")


class Chaishop:
    chai_cls =chai
    def __init__(self):
        self.chai =self.chai_cls("sher")

    def serve(self):
        print(f"serving {self.chai.type} chai in")
        self.chai.prepare()

class fancy(Chaishop):
    chai_cls = mas


shop =Chaishop()
fancy = fancy()
shop.serve()
fancy.serve()




