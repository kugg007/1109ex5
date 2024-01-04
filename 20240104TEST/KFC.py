class fried_chicken:
    #建立類別
    def __init__(self,price,money,cooktime,size,spices,parts):
        self.price = price
        self.money = money
        self.cooktime = cooktime
        self.size = size
        self.spices = spices
        self.parts = parts

    #客人買東西 判斷尺寸大小/部位 將客人付的錢扣掉價格後找錢
    def buy(self):
        if self.size == "BIG":
            self.price1 = 50
        if self.size == "SMALL":
            self.price1 = 30
        if self.parts == "LEG":
            self.price2 = 3
        if self.parts == "WINGS":
            self.price2 = 2
        self.money = self.money - (self.price1 * self.price2)
        print(f"找{self.money}$") 

    #等待時間 判斷尺寸大小/部位 看要炸多久
    def waittime(self):
        if self.size == "BIG":
            self.cooktime1 = 120
        if self.size == "SMALL":
            self.cooktime1 = 60
        if self.parts == "LEG":
            self.cooktime2 = 5
        if self.parts == "WINGS":
            self.cooktime2 = 4
        self.cooktime = self.cooktime1 * self.cooktime2
        print(f"需要等{self.cooktime}秒")

    #口味 判斷口味選擇 給予回覆
    def taste(self):
        if self.spices == "SWEET":
            print(f"你是台南人?")
        if self.spices == "SPICY":
            print(f"辣啦")
        if self.spices == "ALL":
            print(f"It's sweet but spicy")

#設定客人起始值
bob1 = fried_chicken(0, 1000, 0, "BIG","SWEET","LEG")
bob2 = fried_chicken(0, 500, 0, "SMALL","SPICY","LEG")
bob3 = fried_chicken(0, 300, 0, "BIG","SPICY","WINGS")
bob4 = fried_chicken(0, 250, 0, "SMALL","ALL","WINGS")

#呼叫函式
print("**********")
bob1.buy()
bob2.buy()
bob3.buy()
bob4.buy()
print("**********")
bob1.waittime()
bob2.waittime()
bob3.waittime()
bob4.waittime()
print("**********")
bob1.taste()
bob2.taste()
bob3.taste()
bob4.taste()
print("**********")