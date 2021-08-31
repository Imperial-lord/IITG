format long e;
N = 20:20:160;
N_list = []; norm_list = []; 
genp_L = []; genp_U = [];
gepp_L = []; gepp_U = [];
genp_ratio = []; gepp_ratio = [];
for n = N
    for i = [1 2 inf]
        A = rand(n);
        A(1, 1) = 50*eps*A(1, 1);
        
        [L, U] = genp(A);
        [L1, U1, p] = gepp(A);
        
        N_list = [N_list; n];
        norm_list = [norm_list; i];
        genp_L = [genp_L; norm(L, i)];
        genp_U = [genp_U; norm(U, i)];
        gepp_L = [gepp_L; norm(L1, i)];
        gepp_U = [gepp_U; norm(U1, i)];
        genp_ratio = [genp_ratio; norm((L*U-A), i)/norm(A, i)];
        gepp_ratio = [gepp_ratio; norm(L1*U1-A(p, :), i)/norm(A, i)];
        save("q5_workspace_N="+num2str(n)+"_Norm="+num2str(i));
    end
end
T = table(N_list, norm_list, genp_L, genp_U, genp_ratio, gepp_L, gepp_U, gepp_ratio, 'VariableNames', {'Size', 'Norm Type', 'GENP L', 'GENP U', 'GENP ratio', 'GEPP L', 'GEPP U', 'GEPP ratio'});
disp(T);