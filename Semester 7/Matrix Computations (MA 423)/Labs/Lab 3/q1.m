format long e;

C = [];
C_1_norm = [];
C_inf_norm = [];
N = 2:2:16;
for n=N
    H = hilb(n);
    C = [C; cond(H)];
    C_1_norm = [C_1_norm; cond(H,1)];
    C_inf_norm = [C_inf_norm; cond(H,inf)];
    save("q1_workspace_N="+num2str(n));
end

figure;
semilogy(N,C);
xlabel('N');
ylabel('Condition number');
title('2-norm');

figure;
semilogy(N,C_1_norm);
xlabel('N');
ylabel('Condition number');
title('1-norm');

figure;
semilogy(N,C_inf_norm);
xlabel('N');
ylabel('Condition Number');
title('inf-norm');