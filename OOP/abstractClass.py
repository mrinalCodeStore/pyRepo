class a():
    #@abstractmethod
    def calc(self,x):
        pass

class b(a):
    def calc(self,x):
        print('the square is: ',x*x)

o1=b()
o1.calc(10)
