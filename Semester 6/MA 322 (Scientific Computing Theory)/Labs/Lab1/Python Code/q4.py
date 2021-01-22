import math

#Question 4

def f(x):
    return x/2-math.sin(x)

def df(x):
    return 1/2-math.cos(x)

# Using Bisection
a=math.pi/2
b=math.pi
err=0.5*10**(-2)

n=(math.log(b-a)-math.log(err))/math.log(2)
n=math.ceil(n)

mid=a
for i in range(0,n):
    mid=(a+b)/2
    if(f(a)*f(mid)<0):
        b=mid
    else:
        a=mid
print("The epsilon we're taking for Bisection method = {}".format(err))
print("a. Bisection's approximate root = {root}".format(root=mid))

# Using Fixed Point Iteration
# x=g(x).. choose g(x) = sinx+x/2 --> because this will ensure [g(a),g(b)] is subset of [a,b]

# x(n+1) = g(x(n)) or x(n+1)=sinx(n) + x(n)/2
x1=mid
def findx2(x1):
    return math.sin(x1)+x1/2

def findq(a,b,c,d):
    num=math.log(abs((d-c)/(c-b)))
    denom=math.log(abs((c-b)/(b-a)))
    if(denom==0): 
        return "error"
    return num/denom

eps=10**(-6)
x2=findx2(x1)
X=[x1,x2]
x1=x2
x2=findx2(x1)
X.append(x2)
x1=x2
x2=findx2(x1)
X.append(x2)
Q=[]
Q.append(findq(X[0],X[1],X[2],X[3]))
itr=2
while(1):
    itr+=1
    x1=x2
    x2=findx2(x1)
    X.append(x2)
    
    temp=(findq(X[itr-2],X[itr-1],X[itr],X[itr+1]))
    if(temp=="error" or temp==0):
        break
    Q.append(temp)
    if(abs(Q[itr-2]-Q[itr-3])<eps):
        break
print("For fixed point iteration we'll take x=g(x), with g(x)=sinx+x/2." 
      "\nNote that this will ensure all criteria are satisfied since g(x) will in [pi/2,pi]")
print("b. The order of convergence = {order}".format(order=round(Q[itr-2])))
