'''
Kailen Hargenrader
2/4/20
Polynomial AROC
Collects coefficients and constant for 5 degree polynomial, finds x intercepts, finds AROC, finds turning points, and sees if graph is increasing or decreasing at x = -10 and x = 7.
'''

#asks for coefficient values and constant
coef = ["a","b","c","d","e","f"]
for x in range(len(coef)):
  coef[x]=float(input("Enter value for " + coef[x] + ": "))
xvalues = []
yvalues = []
xholder = -20

#creates list of all x valeus -20 to 20 with step .25, creates list of corresponding y values.
for x in range(161):
  xvalues.append(xholder)
  y = coef[0]*xholder**5+coef[1]*xholder**4+coef[2]*xholder**3+coef[3]*xholder**2+coef[4]*xholder+coef[5]
  yvalues.append(y)
  xholder += .25
print("")

#finds x-intercepts (or estimates).
con1 = 1
aroc = []
tp = []
for z in range(160):
  aroc.append((yvalues[z+1]-yvalues[z])/(xvalues[z+1]-xvalues[z]))
  if yvalues[z]>0 and yvalues[z+1]<0:
    xplus1 = xvalues[z+1]
    xhalf = xvalues[z]+0.125
    yhalf = coef[0]*xhalf**5+coef[1]*xhalf**4+coef[2]*xhalf**3+coef[3]*xhalf**2+coef[4]*xhalf+coef[5]
    if yhalf > 0:
      print("There is an x-intercept at x = "+str(xplus1))
      con1 = 2
    elif yhalf < 0:
      print("There is an x-intercept at x = "+str(xvalues[z]))
      con1 = 2
    else:
      print("There is an x-intercept at x = "+ str(xhalf))
      con1 = 2
  if yvalues[z]<0 and yvalues[z+1]>0:
    xplus1 = xvalues[z+1]
    xhalf = xvalues[z]+0.125
    yhalf = coef[0]*xhalf**5+coef[1]*xhalf**4+coef[2]*xhalf**3+coef[3]*xhalf**2+coef[4]*xhalf+coef[5]
    if yhalf > 0:
      print("There is an x-intercept at x = "+str(xvalues[z]))
      con1 = 2
    elif yhalf < 0:
      print("There is an x-intercept at x = "+str(xplus1))
      con1 = 2
    else:
      print("There is an x-intercept at x = "+ str(xhalf))
      con1 = 2
  if yvalues[z] == 0:
    print("There is an x-intercept at x = " + str(xvalues[z]))
    con1 = 2
if con1 == 1:
  print("There are no x intercepts!")

# finds turning points
for z in range(159):
  if aroc[z]*aroc[z+1] < 0:
    arochalf = (yvalues[z+2]-yvalues[z+1])/(xvalues[z+2]-xvalues[z+1])
    if arochalf * aroc[z] > 0:
      print("Turning point at (" + str(xvalues[z+2])+","+str(yvalues[z+2])+")")
    elif arochalf * aroc[z] < 0:
      print("Turning point at (" + str(xvalues[z+1])+","+str(yvalues[z+1])+")")
print("")

#finds if graph is increasing or decreasing at x = -10 and x = 7.
if aroc[40]<0 and aroc[41]<0 and aroc[42]<0:
  print("at x = -10 your polynomial is decreasing!")
elif aroc[40]>0 and aroc[41]>0 and aroc[42]>0:
  print("at x = -10 your polynomial is increasing!")
else:
  print("at x = -10 your polynomial has a turning point!")
if aroc[148]<0 and aroc[149]<0 and aroc[150]<0:
  print("at x = 7 your polynomial is decreasing!")
elif aroc[148]>0 and aroc[149]>0 and aroc[150]>0:
  print("at x = 7 your polynomial is increasing!")
else:
  print("at x = 7 your polynomial has a turning point!")
print("")
print("--------Hope this is what you were looking for!-----------")
