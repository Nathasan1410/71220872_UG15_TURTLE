import turtle


s = turtle.Screen()
t = turtle.Turtle()
t.pensize(3)

def N():
    t.penup ()
    t.goto(-300, 0)
    t.pendown ()
    t.left(90)
    t.forward(100)
    t.right(135)
    t.forward(140)
    t.left(135)
    t.forward(100)

def spasi1 ():
    t.right(90)
    t.penup()
    t.forward(50)
    t.pendown()

def tujuh():
    t.forward(75)
    t.right(115)
    t.forward(120)

def spasi2():
    t.left(115)
    t.penup()
    t.forward(105)
    t.pendown()

def delapan():
    for i in range (54) :
        t.forward(5)
        t.left(10)
    for i in range (36) :
        t.forward(5)
        t.right(10)

def spasi3():
    t.penup()
    t.left(180)
    t.forward(30)
    t.left(40)
    t.forward(45)
    t.right(40)
    t.left(25)
    t.pendown()
    
def dua():
    t.left(40)
    for i in range (20):
        t.forward(6)
        t.right(10)
    t.forward(75)
    t.left(135)
    t.forward(75)

def spasi4 ():
    t.penup()
    t.forward(40)
    t.pendown()

def S():
    t.forward(20)
    for i in range (18):
        t.forward(5)
        t.left(10)
    for i in range (18):
        t.forward(5)
        t.right(10)
    t.forward(25)

def background():
    screen = turtle.Screen()
    screen.setup(600,400)
    screen.bgpic('c57.gif')


N()
spasi1()
tujuh()
spasi2()
delapan()
spasi3()
dua()
spasi4()
S()
background()

t.screen.exitonclick()
