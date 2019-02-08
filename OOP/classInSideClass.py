class outer:
    def __init__(self,leng,bred):
        self.length=leng
        self.breadth=bred
        self.show()

    class inner:
        def __init__(self,col):
            self.color=col
            self.show()
            
        def show(self):
            print('color is ', self.color)

    def show(self):
        print('length is: ',self.length, 'breadth is ', self.breadth)


outerObj1=outer(10,5)
innerObj1=outer.inner('red')
