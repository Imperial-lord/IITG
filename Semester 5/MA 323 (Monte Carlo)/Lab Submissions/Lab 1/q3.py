import matplotlib.pyplot as plt 

x_cor=[]
y_cor=[]
def print_table(a,b,m):
    x=1 #assuming x0=1 in this case. We also observe that the graph does not change pattern by varying x0.
    temp=x
    for y in range(0,m+1):
        temp1=temp
        temp=(temp1*a+b)%m
        x_cor.append(temp1/m)
        y_cor.append(x/m)
        if(temp==x):
            break

a=1229
b=1
m=2048
print_table(a,b,m)
plt.plot(x_cor,y_cor)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Question 3')
plt.show()
