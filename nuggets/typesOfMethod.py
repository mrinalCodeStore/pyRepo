class c1:

    a=10
    
    def __init__(self):
        self.a=12

    def inUpdate(self,a):
        self.a=a

    def clUpdate(cls,a):
        cls.a=a

    def showVal(self,cls):
        print('the class variable a is',cls.a)
        print('the instance variable a is',self.a)
        

obj1=c1()
obj1.showVal(c1)

obj1.inUpdate(13)
c1.clUpdate(c1,11)

obj1.showVal(c1)
