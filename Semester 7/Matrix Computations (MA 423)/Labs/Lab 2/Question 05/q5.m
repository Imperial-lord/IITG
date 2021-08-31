% Setting the numeric format in the command window
format long;

n_values=[]; norm_difference = [];
% Generating random matrices for sizes 5 to 10
for n=5:10
    X = randn(n);
    
    % construct a symmetric matrix using either
    A = 0.5*(X+X');
    % since A(i,j) < 1 by construction and a symmetric diagonally dominant matrix
    % is symmetric positive definite, which can be ensured by adding nI
    A = A + n*eye(n);
    
    % Using the mychol(A) function to generate the Cholesky Factor
    G = mychol(A);
    % Using the built-in MATLAB function to generate the Cholesky Factor
    G1 = chol(A);
    
    n_values = [n_values n];
    norm_difference = [norm_difference norm(G-G1)];
end

n_values = n_values'; norm_difference =  norm_difference';
T = table(round(n_values), norm_difference);
disp(T);