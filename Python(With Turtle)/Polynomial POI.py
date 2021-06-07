'''
Kailen Hargenrader
2/4/20
Polynomial AROC
Collects coefficients and constant and step size for 5 degree polynomial, finds x intercepts,
finds IROC, turning points, POIs, tangent line at 2 random points.
'''

import random

#asks for coefficient values and constant
coef = ["a","b","c","d","e","f"]
for x in range(len(coef)):
  coef[x]=float(input("Enter value for " + coef[x] + ": "))
xvalues = []
yvalues = []
xholder = -20

#creates list of all x values -20 to 20 with step inputed by user, creates list of corresponding y values.
stepsize = float(input("What step size would you like to use?: "))
Range = int(40 / stepsize + 1)
for x in range(Range):
  xvalues.append(xholder)
  y = coef[0]*xholder**5+coef[1]*xholder**4+coef[2]*xholder**3+coef[3]*xholder**2+coef[4]*xholder+coef[5]
  yvalues.append(y)
  xholder = xholder + stepsize
  
  if xholder > 0 and xholder < 0.00001:
    xholder = 0

#creates list of irocs and second derivative
iroc = []
irocroc = []
for z in range(Range):
  iroc.append(5*coef[0]*xvalues[z]**4+4*coef[1]*xvalues[z]**3+3*coef[2]*xvalues[z]**2+2*coef[3]*xvalues[z]+coef[4])
  doubleprime = 20*coef[0]*xvalues[z]**3+12*coef[1]*xvalues[z]**2+6*coef[2]*xvalues[z]+coef[3]
  irocroc.append(doubleprime)
  
#finds x-intercepts (or estimates).
con1 = 1
tp = []
for z in range(Range-1):
  if yvalues[z]>0 and yvalues[z+1]<0:
    xplus1 = xvalues[z+1]
    xhalf = xvalues[z]+stepsize/2
    yhalf = coef[0]*xhalf**5+coef[1]*xhalf**4+coef[2]*xhalf**3+coef[3]*xhalf**2+coef[4]*xhalf+coef[5]
    if yhalf > 0:
      xplus1 = round(xplus1, 4)
      print("There is an x-intercept at x = "+str(xplus1))
      con1 = 2
    elif yhalf < 0:
      xvalues[z] = round(xvalues[z], 4)
      print("There is an x-intercept at x = "+str(xvalues[z]))
      con1 = 2
    else:
      xhalf = round(xhalf, 4)
      print("There is an x-intercept at x = "+ str(xhalf))
      con1 = 2
  if yvalues[z]<0 and yvalues[z+1]>0:
    xplus1 = xvalues[z+1]
    xhalf = xvalues[z]+stepsize/2
    yhalf = coef[0]*xhalf**5+coef[1]*xhalf**4+coef[2]*xhalf**3+coef[3]*xhalf**2+coef[4]*xhalf+coef[5]
    if yhalf > 0:
      xvalues[z] = round(xvalues[z], 4)
      print("There is an x-intercept at x = "+str(xvalues[z]))
      con1 = 2
    elif yhalf < 0:
      xplus1 = round(xplus1, 4)
      print("There is an x-intercept at x = "+str(xplus1))
      con1 = 2
    else:
      xhalf = round(xhalf, 4)
      print("There is an x-intercept at x = "+ str(xhalf))
      con1 = 2
  if yvalues[z] == 0:
    xvalues[z] = round(xvalues[z], 4)
    print("There is an x-intercept at x = " + str(xvalues[z]))
    con1 = 2
if con1 == 1:
  print("There are no x intercepts!")
  
# finds turning points
for z in range(Range-1):
  if iroc[z]*iroc[z+1] < 0:
    irocholder = xvalues[z]+stepsize/2
    irochalf = 5*coef[0]*irocholder**4+4*coef[1]*irocholder**3+3*coef[2]*irocholder**2+2*coef[3]*irocholder+coef[4]
    if irochalf * iroc[z] > 0:
      xvalues[z+1] = round(xvalues[z+1], 4)
      yvalues[z+1] = round(yvalues[z+1], 4)
      print("Turning point at (" + str(xvalues[z+1])+", "+str(yvalues[z+1])+")")
    elif irochalf * iroc[z] < 0:
      xvalues[z] = round(xvalues[z], 4)
      yvalues[z] = round(yvalues[z], 4)
      print("Turning point at (" + str(xvalues[z])+", "+str(yvalues[z])+")")
  if iroc[z]==0:
    xvalues[z] = round(xvalues[z], 4)
    yvalues[z] = round(yvalues[z], 4)
    print("Turning point at (" + str(xvalues[z])+", "+str(yvalues[z])+")")
print("")


#finds POIs
for z in range(Range-1):
  if irocroc[z]*irocroc[z+1] < 0:
    irocrocholder = xvalues[z]+stepsize/2
    irocrochalf = 20*coef[0]*irocrocholder**3+12*coef[1]*irocrocholder**2+6*coef[2]*irocrocholder+coef[3]
    if irocrochalf * irocroc[z] > 0:
      xvalues[z+1] = round(xvalues[z+1], 4)
      yvalues[z+1] = round(yvalues[z+1], 4)
      print("POI at (" + str(xvalues[z+1])+", "+str(yvalues[z+1])+")")
    elif irocrochalf * irocroc[z] < 0:
      xvalues[z] = round(xvalues[z], 4)
      yvalues[z] = round(yvalues[z], 4)
      print("POI at (" + str(xvalues[z])+", "+str(yvalues[z])+")")
  if irocroc[z]==0:
    xvalues[z] = round(xvalues[z], 4)
    yvalues[z] = round(yvalues[z], 4)
    print("POI at (" + str(xvalues[z])+", "+str(yvalues[z])+")")
print("")

#finds tangent line at 2 random x values
tanx = random.uniform(-20, 20)
tanx2 = random.uniform(-20, 20)
tany = coef[0]*tanx**5+coef[1]*tanx**4+coef[2]*tanx**3+coef[3]*tanx**2+coef[4]*tanx+coef[5]
tany2 = coef[0]*tanx2**5+coef[1]*tanx2**4+coef[2]*tanx2**3+coef[3]*tanx2**2+coef[4]*tanx2+coef[5]
tand = 5*coef[0]*tanx**4+4*coef[1]*tanx**3+3*coef[2]*tanx**2+2*coef[3]*tanx+coef[4]
tand2 = 5*coef[0]*tanx2**4+4*coef[1]*tanx2**3+3*coef[2]*tanx2**2+2*coef[3]*tanx2+coef[4]
tanx = round(tanx, 4)
tanx2 = round(tanx2, 4)
tany = round(tany, 4)
tany2 = round(tany2, 4)
tand = round(tand, 4)
tand2 = round(tand2, 4)

print("The tangent line at point (" + str(tanx) + ", " + str(tany) + ") is")
print("y - " + str(tany) + " = " + str(tand) + "(x - " + str(tanx) + " )")
print("The tangent line at point (" + str(tanx2) + ", " + str(tany2) + ") is")
print("y - " + str(tany2) + " = " + str(tand2) + "(x - " + str(tanx2) + " )")
