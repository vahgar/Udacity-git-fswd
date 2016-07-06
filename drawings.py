import turtle

window = turtle.Screen()
window.bgcolor("red")
brad = turtle.Turtle()
def draw_square(brad):
    for i in range(1,5):
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
 

def draw_art():
    brad = turtle.Turtle()
    for i in range(1,36):
        draw_square(brad)
        brad.right(10)
        

    window.exitonclick()

draw_art()
