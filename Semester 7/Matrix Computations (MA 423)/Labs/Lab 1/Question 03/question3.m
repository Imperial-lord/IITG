% Store the time taken for matrix of each sizes 200 to 1150
T_Gauss = [];
T_Inverse = [];

for i=linspace(200,1150,20)
    A = randn(i);
    b = randn(i,1);
    tic;
    % Time taken for Gaussian elimination
    x = A\b;
    T_Gauss = [T_Gauss; toc];
    % Time taken using Inverse 
    tic;
    x = inv(A)*b;
    T_Inverse = [T_Inverse; toc];
    
end


semilogx(linspace(200,1150,20), T_Gauss);
hold on;
semilogx(linspace(200,1150,20), T_Inverse);
legend('Gaussian', 'Inverse');
xlabel('Size of the matrix');
ylabel('Time elapsed');