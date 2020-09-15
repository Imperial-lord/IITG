import matplotlib.pyplot as plt
u=[]

def generate_first_17():
    #X(i+1)=(X(i)A + B) mod M and U(i+1)=X(i+1)/M -> Linear Congruence Generator
    x=23 # x0 value
    m=4096
    a=17
    for i in range(0,17):
        u.append(x/m)
        t=(a*x+1)%m #b=1
        x=t

def fib_genforu():
    #U(i+1)=U(i-17)-U(i-5) and U(i)=U(i)+1 (if U(i)<0) -> Lagged Fiboniacci Generator
    for i in range(17,100000):
        t=u[i-17]-u[i-5]
        if(t<0):
            t=t+1
        u.append(t)

def plot_graph(l):
    x_cor=[]
    y_cor=[]
    no_values=len(l)-1
    if(len(l)==100000):
        no_values=len(l)
    for i in range(0,len(l)-1):
        x_cor.append(l[i])
        y_cor.append(l[i+1])
    plt.scatter(x_cor,y_cor,s=5)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plot (U(i), U(i+1)) for '+str(no_values)+' values of U')
    plt.show()

def plot_hist(l):
    l.sort()
    no_values=len(l)-1
    if(len(l)==100000):
        no_values=len(l)
    label_hist='Histogram for '+str(no_values)+' values of U'
    plt.hist(l, bins=20, rwidth=0.85, color='#FFD600') #bins fixed at 20
    plt.title(label_hist)
    plt.xlabel('Values')
    plt.ylabel('Frequency')
    plt.show()

generate_first_17()
fib_genforu()
plot_graph(u[0:1001])
plot_hist(u[0:1001])
plot_graph(u[0:10001])
plot_hist(u[0:10001])
plot_graph(u[0:100001])
plot_hist(u[0:100001])
