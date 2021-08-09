% function to generate a Hamiltonian Matrix of size n
function HamiltonMatrix = Hamiltonian(n)
    H11 = randn(floor(n/2));
    H11 = diag(diag(H11)) + tril(H11, -1)+tril(H11, -1)';
    H12 = randn(floor(n/2));
    H12 = diag(diag(H12)) + tril(H12, -1)+tril(H12, -1)';
    
    HamiltonMatrix = [H11 H12; H12 -H11];
end