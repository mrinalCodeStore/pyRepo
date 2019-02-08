class c1:
    a=11
    def __init__(self):
        self.a=10
    def showVal(self,cls):
        print('class variable for ',cls.a)
        print('instance variable ',self.a)
    
    
obj1=c1()
obj2=c1()
print('---------------------------------------')
obj1.showVal(c1)

obj2.showVal(c1)
print('---------------------------------------')

obj1.a=12 #instance variable updated 
c1.a=13 #class variable updated
print('---------------------------------------')

obj1.showVal(c1)

obj2.showVal(c1)
print('---------------------------------------')
