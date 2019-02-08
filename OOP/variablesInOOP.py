class base:
    a=9      #class or static variable
    def __init__(self,b,c):
        self.b=b   # instance variable
        self.c=c   # instance variable

    def showVal(self):
        print('a ',self.a)
        print('b ',self.b)
        print('c ',self.c)

obj1=base(2,3)
obj2=base(4,5)


base.a=10
base.b=6
obj1.showVal()
obj2.showVal()

