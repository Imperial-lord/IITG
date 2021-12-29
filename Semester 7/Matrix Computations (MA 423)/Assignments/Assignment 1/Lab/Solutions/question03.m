format long;

x = 1; k = 0;
while x+x > x
    x = 2*x; 
    k = k+1;
end

T = table(x,k);
disp(T);

%{ 
    On running the given code, the loop ends execution when k = 1024 and x = inf.
    At ith iteration the value of x is . When the value of k is 1023, the corresponding 
    value of x has 308 decimal digits.
    On the subsequent iteration, i.e. k = 1024, the value of x exceeds the 
    maximum representable value in IEEE 64 bit representation. 
    Since ‘Round-to-Nearest’ is followed, on exceeding N-max, the value of x is rounded to inf.
    This breaks the condition of the while loop and the execution stops.
%}
