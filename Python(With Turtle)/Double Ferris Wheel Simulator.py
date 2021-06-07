import math
import turtle
rlw = float(input("What is the radius of the larger wheel? "))
rsw = float(input("What is the radius of the smaller wheel? "))
height = float(input("how far off the ground is the small wheel at the bottom? "))
revb = float(input("how long does the big wheel take to complete a revolution(minutes)? "))
revs = float(input("How long does the small wheel take to complete a revolution(minutes)? "))
tbig = turtle.Turtle()
tsmall = turtle.Turtle()
tbig.speed(100)
tsmall.speed(100)

pi = math.pi
cos = math.cos
sin = math.sin

tbig.goto(0, rsw + rlw + height)
tbig.penup()
tbig.goto(0, height + rsw)
tsmall.goto(0, height)
tsmall.color("blue")
angle=2*pi
step = .05
init = 0
count = int(angle/step)+1
tbig.pendown()
tbig.color("red")
#Actually Code

while True:
  init+=step
  #tbig.color(500-30*init,0,30*init)
  tsmall.color(30*init,0,500-30*init)
  tbig.goto(rlw*cos(init-pi/2), rlw*sin(init-pi/2)+ rsw + rlw + height)
  tsmall.goto(rsw*cos((revb/revs)*init-pi/2)+rlw*cos(init-pi/2), rsw*sin((revb/revs)*init-pi/2)+rlw*sin(init-pi/2)+ rsw + rlw + height)
  #print(tbig.ycor - height)
  if tbig.ycor() - (height + rsw) < .05 and tsmall.ycor() - height < .05 and init > 2:
    
    print("broken")
    break
