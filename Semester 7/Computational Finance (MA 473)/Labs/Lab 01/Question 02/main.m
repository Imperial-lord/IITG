function main
    [h,k,n] = input_var();
    m = 1/h; 
    
    %{
        The input values used to plot graphs in report:
        h = 0.025
        k = 0.0025
        n = 3
    %}

    X = (0:n)*k; Y = (0:m)*h;

    fprintf('For the case - f(x) = sin(pi*x):');
    
    % invoking `ftcs` function program with required params
	U = ftcs(h, k, m, n, @fun, @f1, @g1, @g2);
    error_table("ftcs",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'FTCS', 'plots/q2_1.png', 'plots/q2_2.png');
	
    % invoking `btcs` function program with required params
	U = btcs(h, k, m, n, @fun, @f1, @g1, @g2);
    error_table("btcs",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'BTCS', 'plots/q2_3.png', 'plots/q2_4.png');
    
    % invoking 'crank_nicolson` function program with required params
    U = crank_nicolson(h, k, m, n, @fun, @f1, @g1, @g2);
    error_table("cn",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'Crank-Nicolson', 'plots/q2_5.png', 'plots/q2_6.png');
    
    
    fprintf('For the case - f(x) = x*(1-x):');
    
    % invoking `ftcs` function program with required params
	U = ftcs(h, k, m, n, @fun, @f2, @g1, @g2);
    error_table("ftcs",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'FTCS', 'plots/q2_7.png', 'plots/q2_8.png');
	
    % invoking `btcs` function program with required params
	U = btcs(h, k, m, n, @fun, @f2, @g1, @g2);
    error_table("btcs",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'BTCS', 'plots/q2_9.png', 'plots/q2_10.png');
    
    % invoking 'crank_nicolson` function program with required params
    U = crank_nicolson(h, k, m, n, @fun, @f2, @g1, @g2);
    error_table("cn",@fun, @f1, @g1, @g2);
    plot_graphs(X,Y,U, 'Crank-Nicolson', 'plots/q2_11.png', 'plots/q2_12.png');
    
end

% ut - uxx = fun
function [y] = fun(~, ~)
	y = 0;
end

% Boundary conditions
function [y] = f1(x)
	y = sin(pi*x);
end

function [y] = f2(x)
	y = x.*(1-x);
end

function [y] = g1(~)
	y = 0;
end

function [y] = g2(~)
	y = 0;
end
