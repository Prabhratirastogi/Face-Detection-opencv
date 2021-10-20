import turtle
sc = turtle.Screen()
sc.setup(700,700)
spiral = turtle.Turtle()
spiral.speed(10)
sc.bgcolor("black")
col = ["yellow","blue","white","green"]
count = 0
#python coder
for i in range(50):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(col[count])
    if count==3:
        count=0
    else:
        count+=1
