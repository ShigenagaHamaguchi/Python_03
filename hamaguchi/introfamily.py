from introduce import Intro

class IntroInfo(Intro):
    def __init__(self,name,age,cat):
        super().__init__(name,age)
        self.cat = cat
    def cat_out(self):
        return "飼い猫の名前は、"+self.cat+"です"