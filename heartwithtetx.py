import math
from turtle import *

def heart(y):
    return 15 * math.sin(y) ** 3

def hearttwo(h):
    return 12 * math.cos(h) - 5 * math.cos(2 * h) - 2 * math.cos(3 * h) - math.cos(4 * h)

speed(1000)
bgcolor("black")
color("pink")

# Draw the heart shape
for i in range(500):
    goto(heart(i)*10 , hearttwo(i)*10 )

# Move to the middle of the heart
penup()
goto(0, -40)  # Adjust the y-coordinate to position the text

# Write the text in the middle of the heart
write(" I Love You ♥ ", align="center", font=("Arial", 14, "bold"))
goto(0,0)
hideturtle()
done()
