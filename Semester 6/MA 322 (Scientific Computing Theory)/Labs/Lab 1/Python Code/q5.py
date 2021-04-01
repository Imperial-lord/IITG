import math

#Question 5
# Secant method
# x(n+1) = x(n) - f(x(n))*(x(n) - x(n-1))/(f(x(n)) - f(x(n-1)))

err=10**(-5)
def f(x):
    return (math.exp(-x)*(x**2+5*x+2))+1

def evalx2(x1,x0):
    num=x1-x0
    denom=f(x1)-f(x0)
    part2=f(x1)*(num/denom)
    return x1-part2

x0=-1
x1=0 # since f(0)*f(-1) <0
x2=evalx2(x1,x0)

while(abs(x2-x1)>err*(abs(x2))):
    x0=x1
    x1=x2
    x2=evalx2(x1,x0)

print("An approximate root using secant method = {root}".format(root=x2))
