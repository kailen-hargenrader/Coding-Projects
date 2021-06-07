import random
import math
count = 0
for i in range(1000000):
  center = random.random()

  angle = random.uniform(0, math.pi)

  topy= center + math.sin(angle)/2
  boty= center - math.sin(angle)/2
  if topy >= 1 and boty <=1 or topy>= 0 and boty <= 0:
    count+=1
print(count)
    
