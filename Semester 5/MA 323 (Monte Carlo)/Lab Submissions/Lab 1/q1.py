def print_table(a,b,m):
    print('a b m  x \tsequence',end='\n\n')
    for x in range(0,11):
        print(a,b,m,x, end='\t')
        temp=x
        for y in range(0,m+1):
            print("{:.2f}".format(temp/m),end=' | ')
            temp1=temp
            temp=(temp1*a+b)%m
            if(temp==x):
                print("{:.2f}".format(x/m),'...'),
                break
print_table(3,0,11)
print('\n')
print_table(6,0,11)

