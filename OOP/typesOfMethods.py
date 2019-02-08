class base:
    a=10                #class variables
    def __init__(self,b):
        self.b=b        #instance variable

    

    @classmethod
    def get_a(cls):         #class method
        print(cls.a)

    def get_b(self):        #instance method
        print(self.b)

    @staticmethod           #static method
    def infor():
        print('Nothing to do with the class or instance')

obj1=base(11)

obj1.get_b()
base.get_a()

base.infor()

    
