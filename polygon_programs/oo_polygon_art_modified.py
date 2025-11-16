import turtle
import random
# For window purpose
import tkinter as tk
from tkinter import ttk


class set_things_up:    
    def __init__(self):
        self.selections = [f"Exhibit {i}" for i in range(1,10)]
        self.select = '1'
        # self.track = 1

    def get_selection(self):
        return self.select

    def update_select(self, valu):
        self.select = valu.replace("Exhibit", '').strip()

    def setup_screen(self):
        # For dropdown
        def select(event):
            selected_item = combo_box.get()
            self.update_select(selected_item)
            # self.track += 1
            label.config(text=txt_choose + "\n\n" + selected_item)

        # Create Screen
        screen = turtle.Screen()    
        # Set-up bg
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)    
        canvas = screen.getcanvas()

        # Create a label
        txt_choose = "Which art do you want to generate? Enter a number between 1 to 9 inclusive:"
        label = tk.Label(canvas.master, text=txt_choose)
        label.pack(pady=8)

        # Create a Combobox widget
        combo_box = ttk.Combobox(canvas.master, values=self.selections, state='readonly')
        combo_box.pack(pady=5)

        # Set default value
        combo_box.set("Exhibit 1")

        # Bind event to selection
        combo_box.bind("<<ComboboxSelected>>", select)

        return screen

class Draw:
    def __init__(self):                
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


def main():
    scr_set = set_things_up()
    pic = Draw()

    scr = scr_set.setup_screen()

    s_track = scr_set.get_selection()
    # c_track = scr_set.track

    def check_for_change():
        nonlocal s_track                     
        s_current = scr_set.get_selection()
        # c_current = scr_set.track
        # If they are not the same
        if s_current != s_track :
            turtle.clear()
            # Handling all 9 modes
            comms = s_current            
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
            # Update Tracking
            s_track = s_current 
        scr.ontimer(check_for_change, 500)

    check_for_change()
    scr.mainloop()

# Maiin Program
if __name__ == "__main__":
    main()    
    