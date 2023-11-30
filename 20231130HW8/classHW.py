class Student:
    def __init__(self) -> None:
        pass

    def getschoolname(self):
        print(self.school)
    def setschoolname(self,school):
        self.school = school

    def getschool_adress(self):
        print(self.school_adress)
    def setschool_adress(self,school_adress):
        self.school_adress = school_adress

    def getdepartmentname(self):
        print(self.department)
    def setdepartmentname(self,department):
        self.department = department

    def getdcn(self):
        print(self.dcn)
    def setdcn(self,dcn):
        self.dcn = dcn

    def getsname(self):
        print(self.sname)
    def setsname(self,sname):
        self.sname = sname

    def getsid(self):
        print(self.sid)
    def setsid(self,sid):
        self.sid = sid

    def getadress(self):
        print(self.adress)
    def setadress(self,adress):
        self.adress = adress

    def getscore(self):
        print(self.score)
    def setscore(self,score):
        self.score = score

    def getGPA(self):
        print(self.GPA)
    def setGPA(self,GPA):
        self.GPA = GPA
    
bob = Student()

bob.setschoolname('STUST')
bob.setschool_adress('tainan')
bob.setdepartmentname('computer')
bob.setdcn('gay')
bob.setsname('jaja')
bob.setsid('4B0G0000')
bob.setadress('taiwan')
bob.setscore(43)
bob.setGPA(4.3)

print("\n----------")
bob.getschoolname()
bob.getschool_adress()
bob.getdepartmentname()
bob.getdcn()
bob.getsname()
bob.getsid()
bob.getadress()
bob.getscore()
bob.getGPA()
print("----------\n")