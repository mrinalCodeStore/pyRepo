class book:
    def __init__(self,val):
        self.value=val

    def __add__(self,other):
        return self.value+other.value

    def __sub__(self,other):
        return self.value*other.value

o1=book(120)
o2=book(100)

print('The operator ',o1+o2)
print('The operator ',o1-o2)
