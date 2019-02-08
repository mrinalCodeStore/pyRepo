#   self is a default variable of a class that contain the memory address of the
#   instance of the current class. so self can be used to refer all the instance variable
#   and instance method
#   It does not have to be named self , you can call it whatever you like,
#   but it has to be the first parameter of any function in the class:
class a:
    def __init__(self):
        self.va=10
        self.vb=3
        print(self)

obj1=a();
print(obj1)

# the address of obj1 and the self keyword is same and refers same object
