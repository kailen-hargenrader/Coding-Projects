'''
Kailen Hargenrader
Hypergeometric Simulator
11/22/2020
This code will simulate marbles drawn out of a bag, the number of marbles in the bag, drawn, and drawn of the chosen color are inputs and the probability of the number drawn is the output.
'''
import random

#input
N = int(input("How many total marbles?: "))
K = int(input("How many are of the type you want?: "))
n = int(input("How many marbles should be drawn? (if greater than the total, then all marbles will be drawn): "))
if n > N:
  n = N

#probability variables
counts = []
for i in range(K+1):
  counts.append(0)

#simulation
for i in range(10000):
  LIST = []
  numb1 = 0
  for i in range(N):
    LIST.append(0);
  for i in range(K):
    LIST[i] = 1
  for i in range(n):
    pick = random.randint(0,len(LIST)-1)
    if LIST[pick] == 1:
      numb1 += 1
    LIST.pop(pick)
  counts[numb1] += 1

#print probabilities
for i in range(K+1):
  print("Probability of " + str(i) + " successes = " + str(counts[i]/10000))


