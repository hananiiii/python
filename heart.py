import math 
from turtle import *

import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create the turtle object
heart = turtle.Turtle()
heart.speed(1000)  # Adjust the speed of the turtle

# Define the colors for the gradient
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the heart shape with gradient colors
for i in range(200):
    heart.color(colors[i % len(colors)])  # Cycle through the colors
    heart.forward(i)
    heart.right(91)

# Hide the turtle after drawing
heart.hideturtle()

# Keep the turtle window open until closed by the user
turtle.done()
