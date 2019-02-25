import turtle as tr

arrow = tr.Turtle()

i=10
a=0

while i>0:
    a=0
    for a in range(4):
        arrow.forward(i*10)
        arrow.left(90)
    i-=1
input()