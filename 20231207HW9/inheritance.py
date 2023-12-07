class sports:
    def __init__(self,name):
        self.sname = name

    @property
    def sport_name(self):
        return self.sname

    @sport_name.setter
    def sport_name(self,value):
        self.sname = value

class landsports(sports):
    def __init__(self,name,field):
        super().__init__ (name)
        self.sfield = field

    @property
    def landsports_field(self):
        return self.sfield

class watersports(sports):
    def __init__(self,name,activities):
        super().__init__ (name)
        self._activities = activities

    @property
    def watersports_activities(self):
        return self._activities

if __name__ == "__main__":
    baseball = landsports("baseball","baseball field")
    print(baseball.sport_name)
    print(baseball.landsports_field)
    
    water_walking = watersports("water walking","walk on water")
    print(water_walking.sport_name)
    print(water_walking.watersports_activities)