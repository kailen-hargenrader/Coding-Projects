import math
import turtle

#Defining stuff
t = turtle.Turtle()
t.speed(100)
r = float(input("Input a Radius: "))
h = float(input("Input the distance from the ground: "))
P = float(input("Input amount of minutes per rotation: "))
m = float(input("Input minutes since the rider got on: "))
pi = math.pi
cos = math.cos
sin = math.sin
centery = r+h

#drawing a line + more defining stuff
t.goto(0, centery)
t.penup()
t.goto(0, h)
angle=2*pi*m/P
step = .05
init = 0
count = int(angle/step)+1
t.pendown()

#Actually Code
for i in range(count):
  init+=step
  t.goto(r*cos(init-pi/2), r*sin(init-pi/2)+centery)
