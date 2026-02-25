class Chai:
    def  __init__(self,type_,console):
        self.type = type_
        self.console = console


class another_class(Chai):
    def __init__(self ,type_,console,sher):
        super().__init__(type_,console)
        self.sher = sher