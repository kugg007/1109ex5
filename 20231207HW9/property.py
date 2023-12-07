class ore:
    def __init__(self,oretype,price,ID,amount):
        self.oretype = oretype
        self.price = price
        self.ID = ID
        self.amount = amount


    @property
    def orename(self):
        print(f'"{self.oretype}" was accessed')
        return self.oretype

    @orename.setter
    def orename(self,price):
        print(f'"{self.oretype}" is now "{price}.')
        self.oretype = price

    @orename.deleter
    def orename(self):
        print(f'"{self.oretype}" was accessed.')
        del self.oretype

if __name__ == "__main__":
    myore = ore("gold",100,"gold_ore",64)

    print(myore.orename)
    myore.orename="diamond"
    del myore.orename
    #print(myore.orename)