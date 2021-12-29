% Testing output[Q,R] =reflectqr(A) for various different randomly generated
% matrices A by running [Qhat,Rhat] =qr(A,0) and checking if norm(Q∗R−A),
% norm(Q′∗Q−eye(m)),norm(tril(R,−1)),norm(R−Rhat),and norm(Q−Qhat) are all≈u.

N_values = [4, 5, 8, 15, 17, 21];
M_values = [3, 5, 7, 13, 15, 20];

norms1 = zeros(length(N_values), 1);
norms2 = zeros(length(N_values), 1);
norms3 = zeros(length(N_values), 1);
norms4 = zeros(length(N_values), 1);
norms5 = zeros(length(N_values), 1);

for i=1:length(N_values)
    n = N_values(i);
    m = M_values(i);
    A = randn(n, m);
    
    [Qhat, Rhat] = qr(A, 0);
    [Q, R] = reflectqr(A);
    
    norms1(i) = norm(Q*R - A);
    norms2(i) = norm(Q'*Q - eye(m));
    norms3(i) = norm(tril(R, -1));
    norms4(i) = norm(R - Rhat);
    norms5(i) = norm(Q - Qhat);
end

t = table(N_values', M_values', norms1, norms2, norms3, norms4, norms5, 'VariableNames', {'N', 'M', ' norm(Q*R - A)', 'norm(tr(Q)*Q − eye(m))', 'norm(tril(R, -1))', 'norm(R - Rhat)', 'norm(Q - Qhat)'});
disp(t);