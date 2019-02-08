#function call of a class
class base:
    def __init__(self, nm): #constructor of the class
        print(nm)
        
    def printn(self):
        print("hello there")

obj1 = base("mrinal")

base.printn(obj1)
obj1.printn()
