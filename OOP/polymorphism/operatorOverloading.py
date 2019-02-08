class student:
  def __init__(self, m1, m2):
    self.marks1=m1
    self.marks2=m2

  def __add__(self,other):  #overloadiing the addition operator
    self.marks1=self.marks1+other.marks1
    self.marks2=self.marks2+other.marks2
    s=student(self.marks1, self.marks2)
    return s

  def show(self):
    print(' the values are ', self.marks1, self.marks2)
  
obj1=student(10,20)
obj2=student(30,40)



obj3=obj1+obj2 #overloading the addition operator
obj3.show()
