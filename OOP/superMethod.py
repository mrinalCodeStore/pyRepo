'''
super() is abuilt in method which is usefull to call the super class
constructor or methods from the sub class
'''

class a:
    def __init__(self,a):
        self.a=a

    def are(self):
        return 3.14*self.a*self.a

    def printv(self):
        print("the value of a: ",self.a)
        

class b(a):
    def __init__(self,b):
        super().__init__(b)  #calls the parent class constructor
        print("the area: ",super().are()) #class the parent class method
        
    
obj1=b(10)
obj1.printv()
