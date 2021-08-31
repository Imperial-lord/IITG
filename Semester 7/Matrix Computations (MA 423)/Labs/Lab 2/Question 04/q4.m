% Setting the numeric format in the command window
format long e;

n=input('Enter the size of matrix A: ');
A = randn(n);

detA = mydet(A);
disp('The determinant of A using mydet() function');
disp(detA);

detA1 = det(A);
disp('The determinant of A using MATLAB inbuilt function')
disp(detA1);

