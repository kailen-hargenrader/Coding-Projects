'''
Birthday Problem Reloaded

OBJECTIVE
Recall that if you have 23 people in a room, there is a 50% chance that at least two of them share a birthday.  Write a program that will graph a histogram of the number of people that it takes to get a matching birthday.

INSTRUCTIONS
Your program should do the following:
- Create a list of random integers between 1 and 365
  - The list should append new values until one of the values is repeated
- Store the length of the list
- Repeat 10000 times
- Use a turtle to draw a histogram of the list lengths
- Calculate and output the average number of people that it takes to get a matching birthday

SAMPLE OUTPUT 

<HISTOGRAM HERE>

On average, you need 24 people in a room for at least two of them to share a birthday.
'''
'''
Kailen Hargenrader
Reverse Birthday Problem
11/22/2020
This code will make a histogram of people needed to have a matching birthday.
'''

import random
import turtle
jeff = turtle.Turtle()
NumPeople = []
placeholder = 0

#runs birthday problem 10,000 times
for i in range(10000):
  Bday = []
  while True:
    int = random.randint(1,365)
    Bday.append(int)
    for j in range(len(Bday)-1):
      if Bday[j] == int:
        placeholder = Bday[j]
        break
    if placeholder == int:
      placeholder = 0
      break
  NumPeople.append(len(Bday))
NumPeople.sort()

#groups similar results
NumOfNumPeople = [0,0]
counter = 0
for k in range(len(NumPeople)):
  if NumPeople[k] == len(NumOfNumPeople):
    counter +=1
  else:
    NumOfNumPeople.append(counter)
    counter = 1
    for l in range(NumPeople[k]-NumPeople[k-1]-1):
      NumOfNumPeople.append(0)
NumOfNumPeople.append(counter)
      
#turtle historgram drawing based on grouped results
jeff.speed(0)
jeff.goto(0,0)
jeff.pendown()
jeff.goto(len(NumOfNumPeople)*10, 0)
jeff.goto(len(NumOfNumPeople)*10, 500)
jeff.goto(0,500)
jeff.fillcolor("black")
for m in range(len(NumOfNumPeople)-1):
  jeff.goto(m*10, 0)
  jeff.begin_fill()
  jeff.goto((m+1)*10, 0)
  jeff.goto((m+1)*10, NumOfNumPeople[m+1])
  jeff.goto(m*10, NumOfNumPeople[m+1])
  jeff.goto(m*10, 0)
  jeff.end_fill()
#resize the turtle window to see the whole histogram, cause I didn't want to make it really small

#outputs the average
counter = 0
for n in range(len(NumOfNumPeople)):
  counter += n*NumOfNumPeople[n]
counter = float(counter)/10000
print("The average number of people is: "+str(counter))


  

