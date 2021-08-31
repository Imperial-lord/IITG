function error_table(flag, fun, f, g1, g2)
% error_table - function to print the error table
% @param - flag, fun, f, g1, g2
% @returns - none

    m=2; h=1/m; k=h^2/2; n=1/k;
    U_prev = error_table_method(flag, h, k, m, n, fun, f, g1, g2);
    Error = []; M = 2;
    while m<=100
        m=m*2;
        h=1/m; k=h^2/2; n=1/k;
        
        U_next = error_table_method(flag, h, k, m, n, fun, f, g1, g2);
        U_next_store = U_next;
        U_next = U_next(1:4:end,1:2:end);
        
        Error = [Error norm(U_prev-U_next,Inf)];
        M = [M m];
        U_prev=U_next_store;
    end
    
    M(end)=[]; Order_of_Convergence = [];
    size(Error);
    for i=1:5
        Order_of_Convergence = [Order_of_Convergence log2(Error(i)/Error(i+1))];
    end
    
    Order_of_Convergence = [Order_of_Convergence NaN];
    
    M=M'; Error=Error'; Order_of_Convergence=Order_of_Convergence';
    T = table(M, Error, Order_of_Convergence);
    disp(T);
end

