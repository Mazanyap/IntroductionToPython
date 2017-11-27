"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alex Mazany.
"""
########################################################################
# Done: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# Done: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg

window = rg.TurtleWindow()

circular_turtle = rg.SimpleTurtle('turtle')
square_turtle = rg.SimpleTurtle('turtle')

circular_turtle.pen = rg.Pen('red', 5)
circular_turtle.speed = 20

square_turtle.pen = rg.Pen('blue', 7)
square_turtle.speed = 20

size = 200

for k in range(7):
    circular_turtle.draw_circle(size)
    circular_turtle.pen_up()
    circular_turtle.left(20)
    circular_turtle.backward(10)
    circular_turtle.right(20)
    circular_turtle.pen_down()

    square_turtle.draw_square(size)
    square_turtle.pen_up()
    square_turtle.right(10)
    square_turtle.backward(10)
    square_turtle.left(30)
    square_turtle.pen_down()

    size = size - 20


