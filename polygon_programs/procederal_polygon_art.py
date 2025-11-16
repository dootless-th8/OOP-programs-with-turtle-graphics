import turtle
import random

def draw_polygon(num_sides, size, orientation, location, color, border_size):
    turtle.penup()
    turtle.goto(location[0], location[1])
    turtle.setheading(orientation)
    turtle.color(color)
    turtle.pensize(border_size)
    turtle.pendown()
    for _ in range(num_sides):
        turtle.forward(size)
        turtle.left(360/num_sides)
    turtle.penup()

def get_new_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def generating_1_shape(shape, fun=False):
    for i in range(random.randint(1, 30)):        
        if fun:
            num_sides = random.randint(3, 5)
        else: num_sides = shape
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

def generating_matrix_shape(shape, fun=False):
    for i in range(random.randint(1, 30)):
        if fun:
            num_sides = random.randint(3, 5)
        else: num_sides = shape
        # num_sides = random.randint(3, 5)
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = get_new_color()
        border_size = random.randint(1, 10)
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        # specify a reduction ratio to draw a smaller polygon inside the one above
        reduction_ratio = 0.618

        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        # adjust the size according to the reduction ratio
        size *= reduction_ratio

        # draw the second polygon embedded inside the original 
        draw_polygon(num_sides, size, orientation, location, color, border_size)

        # reposition the turtle and get a new location
        turtle.penup()
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.left(90)
        turtle.forward(size*(1-reduction_ratio)/2)
        turtle.right(90)
        location[0] = turtle.pos()[0]
        location[1] = turtle.pos()[1]

        # adjust the size according to the reduction ratio
        size *= reduction_ratio

        # draw the second polygon embedded inside the original 
        draw_polygon(num_sides, size, orientation, location, color, border_size)

# Set-up bg
turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

# For 1
def tes1():
    generating_1_shape(3)

# For 2
def tes2():
    generating_1_shape(4)

def tes3():
    generating_1_shape(5)

def tes4():
    generating_1_shape(random.randint(3, 5), True)

def tes5():
    generating_matrix_shape(3)

def tes6():
    generating_matrix_shape(4)

def tes7():
    generating_matrix_shape(5)

def tes8():
    generating_matrix_shape(random.randint(3, 5), True)

def tes9():
    generating_1_shape(3, True)
    generating_matrix_shape(3, True)

tes9()
# hold the window; close it by clicking the window close 'x' mark
turtle.done()