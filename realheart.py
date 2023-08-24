import math 
from turtle import *

def heart(y):
    return 15*math.sin(y)**3
def hearttwo(h):
    return 12*math.cos(h)-5*\
           math.cos(2*h)-2*\
           math.cos(3*h)-\
           math.cos(4*h)
speed(3000)
bgcolor("black")
for i in range(6000) :
    goto(heart(i)*20 ,hearttwo(i)*20)
    for j in range(5):
        color("pink") 
    goto(0,0)
done()