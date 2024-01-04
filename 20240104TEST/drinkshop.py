class drinks:
    def __init__(self,price,milk,boba):
        self.price = price
        self.milk = milk
        self.boba = boba

class employer:
    def __init__(self,name,pay,worktime):
        self.name = name
        self.pay = pay
        self.worktime = worktime
    
class cold(drinks):
    def __init__(self,name,ice,sugra,price,milk,boba):
        super().__init__(price,milk,boba)
        self.name = name
        self.ice = ice
        self.sugra = sugra
        
    @property
    def blacktea(self):
        self.price == 30
        if self.milk=="Y":
            self.name = "milktea"
            self.sugra = "HALF"
            self.price = self.price + 10
        if self.milk=="N":
            self.name = "blacktea"
            self.sugra = "HALF"


class hot(drinks):
    def __init__(self,name,sugra,price,milk,boba):
        super().__init__(price,milk,boba)
        self.name = name
        self.sugra = sugra

    def blacktea(self):
        self.price == 30
        if self.milk=="Y":
            self.name = "milktea"
            self.sugra = "HALF"
            self.price = self.price + 10
        if self.milk=="N":
            self.name = "blacktea"
            self.sugra = "HALF"

bob1 = cold("","","ALL",0,"Y","Y")

print(bob1.blacktea)