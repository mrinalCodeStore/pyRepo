class A:
    def __init__(self):
        print('from constructor of class  a')
    def show(self):
        print("from class a")

class B(A):
    def __init__(self):
        print('from constructor of class b')
    
    def show(self):     #method gets overrided
        print("from class b")

obj1=B()
obj1.show()
