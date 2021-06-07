'''
Kailen Hargenrader
3/6/20
Newton's Method
collects coefficients for 5 degree polynomial, performs Newton
s method on loop until it is accurate to 4 decimal places.
'''

#collects coefficients
coef = ["a","b","c","d","e","f"]
for x in range(len(coef)):
  coef[x]=float(input("Enter value for " + coef[x] + ": "))
xguess = float(input("What is your initial guess for the x-intercept?: "))

#Newton's method loop
xvalues = []
previous = 0
xround = 1
while xround != previous:
  xvalues.append(xguess)
  previous = round(xguess, 4)
  y = coef[0]*xguess**5+coef[1]*xguess**4+coef[2]*xguess**3+coef[3]*xguess**2+coef[4]*xguess+coef[5]
  irocy = 5*coef[0]*xguess**4+4*coef[1]*xguess**3+3*coef[2]*xguess**2+2*coef[3]*xguess+coef[4]
  xguess = xguess - y/irocy
  xround = round(xguess, 4)
  
#Prints Approximation
xvalues.append(xguess)
print(xvalues)
print
print("----------------Also, you forgot to add 5 points back to my previous code.-------------------------")
