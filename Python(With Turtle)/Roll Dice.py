import random
count = 0
number = int(input("How many times would you like to roll 2 dice?: "))

for i in range(number):
  d1 = random.randint(0, 6)
  d2 = random.randint(0, 6)
  if d1 == d2:
    count+= 1
  print(str(d1) + " " + str(d2))
  
print(str(count) + " double(s)")
percent = float(count)*100/number
print(str(percent) + " percent probability of doubles")

#need I comment? I assume its simple enough, also no user protection
