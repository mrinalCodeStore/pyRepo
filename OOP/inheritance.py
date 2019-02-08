class base1:
    def func1(self):
        print('from base1')

class base2:
    def func2(self):
        print('from base2')

class base3(base1):  #single inheritance
    def func3(self):
        pprint('from base3')
        
class derived(base1, base2):  # multiple inheritance
    def func4(self):
        print('from derived')

class derived2(base3): #multilevel inheritance
    def func5(self):
        print('from derived2')

obj1=derived();

obj1.func1()
obj1.func2()
