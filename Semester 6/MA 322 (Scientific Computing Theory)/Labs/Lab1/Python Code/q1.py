import math

#Question 1
# x(n+1) = x(n)*((x(n)**2 + 3*a)/(3*x(n)**2 + a)) --> given iteration

n=0
a=2
x=1
y=2
# To see in [x,y] where x=1 and y=2
def evaluateg(x):
    num=x*(x**2+3*a)
    denom=3*x**2+a
    return num/denom

leftg=evaluateg(x)
rightg=evaluateg(y)
# we have shown that [leftg,rightg] is a subset of [x,y] and g'(x)>0 for all x. Thus, g is monotonically increasing

x0=x #Take x0=1

#Part (a)
x1=evaluateg(x0)
n=n+1
while(abs(x1-x0) > 0.00001):
    x0=x1
    x1=evaluateg(x0)
    n=n+1

print("The value x0 we'll take is = {}".format(x))
print("a. Number of iterations n = {}\n".format(n))

#Part (b)
# For this part we'll note that in [1,2] the functions satisfies all properties for a fixed point iteration
# Since g'(x) is always greater than 0 in [1,2], we can conclude, that order of convergence =1
# We'll now prove this conclusion

def ratioC(alpha,x0,x1):
    return (alpha-x1)/(alpha-x0)

C=[]
alpha = 1.4143 #given in the question
x0=x
x1=evaluateg(x0)
C.append(ratioC(alpha,x0,x1))
itr=0
eps=10**(-11)

while(1):
    itr+=1
    x0=x1
    x1=evaluateg(x0)
    C.append(ratioC(alpha,x0,x1))
    
    if(abs(C[itr]-C[itr-1])<eps):
        break
print("The values of C are:")
print(C)
print("Thus C is tending to a constant i.e, 1 and thus")
print("b. The order of convergence for this case is = 1")
