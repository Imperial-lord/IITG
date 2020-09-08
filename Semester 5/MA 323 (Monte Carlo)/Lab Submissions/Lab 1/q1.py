def print_table(a,b,m):
    print('a b m  x \tsequence',end='\n\n') #print the table headers
    for x in range(0,11):
        print(a,b,m,x, end='\t')
        temp=x
        for y in range(0,m+1):
            print((temp),end=', ')
            temp1=temp
            temp=(temp1*a+b)%m
            if(temp==x):
                print(x,'...'),
                break #we need to stop after we complete the cycle
print_table(3,0,11)
print('\n')
print_table(6,0,11)

