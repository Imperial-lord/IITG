# x(i+1)=(ax(i)+b)%m, u(i+1)=x(i+1)/m
m=2048
def lcg(): #use LCG to generate the point set
    #values to be taken for generating the Uniform RV
    x0=111
    a=1229
    b=11
    
    u_arr=[]
    for i in range(m):
        x1=(a*x0+b)%m
        u1=x1/m
        u_arr.append(u1)
        x0=x1
    return u_arr

def countxinA(x_list,A): #count the number of xs in A
    count=0
    for i in range(len(x_list)):
        x=x_list[i]
        if(x>=A[0] and x<=A[1]):
            count+=1
    return count

N=[10,20,50,100] #The 4 values of N to split the [0,1] interval into N parts
print("Value of N \t Discrepancy")
for i in range(4):
    n=N[i]
    x_list=lcg()
    
    per=1/n
    D=-1 #initialising discrepancy to -1 and then finding the maximum
    for j in range(n):
        A=[j*per,(j+1)*per]
        D=max(D,abs(countxinA(x_list,A)/m-per))
    
    print(str(n)+"\t\t "+str(round(D,6)))
