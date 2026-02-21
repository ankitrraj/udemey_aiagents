class chai:
    def __init__(self,name_):
        self.name = name_

    def print_the(self):
        print(self.name)
        print("sher")

class mas(chai):
    def add_spice(self):
        print("adding chai milk")

class Chaishop:
    chai_cls = chai

    def __init__(self):
        self.chai = self.chai_cls("sher")

    def serve(self):
        print(f"serving {self.chai.name} chai in")
        self.chai.print_the()

class Fancy(Chaishop):
    chai_cls = mas


shop = Chaishop()
fancy_shop = Fancy()

shop.serve()
fancy_shop.serve()
fancy_shop.chai.add_spice()
