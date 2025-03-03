"""
For this program, you will tell Tina the Turtle to draw 
a triangle.

You should look at the previous program, 02_Meet_Tina.py
to see how to use the turtle commands.


"""

# These lines are needed in most turtle programs
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

bob = turtle.Turtle()                  # Create a turtle named bob

# Use bob.forward() and bob.left() to draw a triangle
# Make each side of the triangle a different color with 
# bob.pencolor()

bob.shape('turtle')                    # Set the shape of the turtle to a turtle
bob.speed(2)                           # Your code here

bob.color("cyan")
bob.forward(120)

bob.pencolor("red")
bob.left(90)


bob.pencolor("yellow")
bob.forward(90)

bob.pencolor("orange")
bob.left(127)
bob.forward(147)

bob.pencolor("green")
bob.left(45)

bob.backward(150)


turtle.exitonclick()                    # Close the window when we click on it
