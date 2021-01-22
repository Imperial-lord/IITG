import math

#Question 2
def f(x):
    return (math.tan(math.pi-x)-x)

# take n=[1,10,100,1000,10000,100000]
N=[1,10,100,1000,10000,100000,1000000]
x0=1.6
xn=3
for i in range(7):
    n=N[i]
    X=[x0]
    for j in range(1,n+1):
        X.append(x0+j*1.4/n)
        
    root=x0
    minimum=abs(f(X[0]))
    for j in range(1,n+1):
        f_val=abs(f(X[j])-0)
        if(f_val<minimum):
            minimum=f_val
            root=X[j]
    print("For value n = {n} the root is x = {x}".format(n=n,x=root))
