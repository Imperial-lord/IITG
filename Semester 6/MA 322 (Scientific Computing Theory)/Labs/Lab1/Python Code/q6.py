import math

#Question 6
def f(x):
    return (math.exp(-x)*(x**2+5*x+2))+1

print("Note for questions 6,7 and 8, we have made use of the following formula -"
"\nratio = log(abs((x(k+1)-x(k))/(x(k)-x(k-1))))/log(abs((x(k)-x(k-1))/(x(k-1)-x(k-2))))"
"\norder of convergence = limit of the ratio\n")
# Using Bisection
a=-1
b=0
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

# Using the iterative scheme
# x(n+1) = (x(0)f(x(n)) - x(n)f(x(0)))/(f(x(n))-f(x(0)))

x0=mid
def findx2(x1):
    num=x0*f(x1)-x1*f(x0)
    denom=f(x1)-f(x0)
    return num/denom

def findq(a,b,c,d):
    num=math.log(abs((d-c)/(c-b)))
    denom=math.log(abs((c-b)/(b-a)))
    if(denom==0): 
        return "error"
    return num/denom
    
x1=mid+1
eps=10**(-12)
x2=findx2(x1)
X=[x0,x1,x2]
Q=[]

x1=x2
x2=findx2(x1)
X.append(x2)

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

print("b. The order of convergence = {order}".format(order=round(Q[itr-3])))
