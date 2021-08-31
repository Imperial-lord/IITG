function [U] = error_table_method(flag, h, k, m, n, fun, f, g1, g2)
% error_table_method - function to call the methods based on flag value
% @param - flag, h, k, m, n, fun, f, g1, g2
% @returns - U

    if(flag=="ftcs")
        U = ftcs(h, k, m, n, fun, f, g1, g2);
    elseif(flag=="btcs")
        U = btcs(h, k, m, n, fun, f, g1, g2);
    else
        U = crank_nicolson(h, k, m, n, fun, f, g1, g2);
    end
end

