import math

#Question 3

def f(x):
    return x/2-math.sin(x)

def df(x):
    return 1/2-math.cos(x)

# Using Bisection
a=math.pi/2
b=math.pi
err=0.5*10**(-2)

print("The epsilon we're taking for Bisection method = {}".format(err))

n=(math.log(b-a)-math.log(err))/math.log(2)
n=math.ceil(n)

mid=a
for i in range(0,n):
    mid=(a+b)/2
    if(f(a)*f(mid)<0):
        b=mid
    else:
        a=mid

print("a. Bisection's approximate root = {root}".format(root=mid))

# Usnig Newton's method
# We see that the f'(x) >0 and f''(x)>0 in the range [pi/2,pi]. Thus we'll choose x0=b, and the sequence 
# will converge to α
itnum=1
x0=mid
denom=df(x0)
eps=0.5*10**(-7)

print("The epsilon we're taking for Netwon's method = {}".format(eps))

if(denom==0):
    print("Denominator is 0 for Newton's method in step 1")

else:
    x1=x0-f(x0)/denom

    while(abs(x1-x0)>eps):
        itnum+=1
        x0=x1
        denom=df(x0)
        if(denom==0):
            print("Denominator is 0")
            break
        x1=x0-f(x0)/denom
    root=x1

print("b. Newton's root = {root}".format(root=root))
