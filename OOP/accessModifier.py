class base:
    t=30
    def __init__(self):
        self.a=10
        self.b=12
    

class derived(base):
    
    def printN(self):
        print(super.a)
        #print(super.t)


b=derived()
b.printN()
