import turtle
import random


class Draw:
    def __init__(self):        
        # Set-up bg
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)
        pass
    

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
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


    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    

    def generating_shapes(self, num, many=False, fun=False):
        # Drawing random amount of shapes
        for i in range(random.randint(1, 30)):        
            # For deciding multiple shapes or not.
            if fun:
                num_sides = random.randint(3, 5)
            else: num_sides = num
            # No need editing
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = self.get_new_color()
            border_size = random.randint(1, 10)

            # Draw le thing
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)
            # For making a domino effect
            if many:
                for l in range(2):
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
                    self.draw_polygon(num_sides, size, orientation, location, color, border_size)        

# Main Program
if __name__ == "__main__":                
    comms = input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: ").strip()            
    pic = Draw()
    if comms == '1':
        pic.generating_shapes(3)
    elif comms == '2':
        pic.generating_shapes(4)
    elif comms == '3':
        pic.generating_shapes(5)   
    elif comms == '4':
        pic.generating_shapes(3, False, True) 
    elif comms == '5':
        pic.generating_shapes(3, True)
    elif comms == '6':
        pic.generating_shapes(4, True)
    elif comms == '7':
        pic.generating_shapes(5, True)
    elif comms == '8':
        pic.generating_shapes(3, True, True)
    elif comms == '9':
        pic.generating_shapes(3, False, True)
        pic.generating_shapes(3, True, True)    
    turtle.done()
    