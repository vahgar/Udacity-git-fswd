import turtle

window = turtle.Screen()
window.bgcolor("red")

def draw_square():

    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("yellow")
    brad.speed(1)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)
    brad.forward(100)
    brad.right(90)

    

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("blue")
    angie.circle(100)

 


def draw_triangle():

    leo = turtle.Turtle()
    leo.forward(200)
    leo.left(120)
    leo.forward(200)
    leo.left(120)
    leo.forward(200)
    window.exitonclick()

draw_square()

draw_circle()

draw_triangle()
