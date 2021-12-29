format long e
dep_from_orth=[];
methods={};
condition_number=[];
t = table(methods,condition_number,dep_from_orth,'VariableNames',{'Method','Condition Number','Departure from Orthogonality'});
file={'Q4-1.mat','Q4-2.mat','Q4-3.mat'};

for i=1:3
    load(file{i})
    [Q_cgs,~]=cgs(A);
    [Q_mgs,~]=mgs(A);
    [Q_cgsrep,~]=cgsrep(A);
    [Q,~]=qr(A);
    Im=eye(n);
    dep_from_orth=[norm(Im-Q_cgs'*Q_cgs,2);norm(Im-Q_mgs'*Q_mgs,2);norm(Im-Q_cgsrep'*Q_cgsrep,2);norm(Im-Q'*Q,2)];
    methods={'CGS';'MGS';'CGSREP';'Matlab Command'};
    
    for j=1:4
        t=[t;[methods(j),kappa,dep_from_orth(j)]];
    end
end

disp(t);