"""
The is a simple Turtle program that draws a square and writes a message. The
lines that start with a # are comments. They are not executed by Python. The
lines inside the three quotes are also comments, but of a different sort (
called "doc comments" ) Comments are used to explain what the code does. Read
the program and try to understand what each line does.

RUM ME! YOu can run this program by clicking on ▶️ icon ar the top of the editor
window.

"""

import turtle                        # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

bob =turtle.Turtle()                  # Create a turtle named tina

bob.shape('turtle')                    # Set the shape of the turtle to a turtle
bob.speed(2)                           # Make the turtle move as fast, but not too fast.

bob.pencolor('gold')                   # Set the pen color to blue
bob.forward(150)                       # Move tina forward by the forward distance
bob.left(90)                           # Turn tina left by the left turn

bob.pencolor('yellow')                    # Set the pen color to red
bob.forward(150)                       # Continuie the last two steps three more times
bob.left(90)                           # to draw a square

bob.pencolor('dark cyan')                  # Set the pen color to green
bob.forward(150)
bob.left(90)

bob.pencolor('teal')                 # Set the pen color to purple
bob.forward(150)
bob.left(90)

bob.penup()                            # Lift the pen up so we can move tina without drawing
bob.forward(20)                        # Move tina forward by 20
bob.left(90)                           # Turn tina left by 90 degrees
bob.forward(20)                        # Move tina forward by 20
bob.write("I'm bob,not tina!")         # Write the message "Why, hello there!"
bob.backward(20)                       # Move tina backward by 20

bob.goto(-50,0)
bob.pendown()
bob.color('black')                       # Set the color of tina to red
bob.begin_fill()
bob.circle(101, steps=50)
bob.end_fill()

turtle.exitonclick()                    # Close the window when we click on it

# Now you can try writing your own programs. Open
# the next file 03_Turtle_Tricks.py

