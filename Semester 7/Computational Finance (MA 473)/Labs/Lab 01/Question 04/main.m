function main
    [h,k,n] = input_var();
    m = 1/h; 
    
    %{
        The input values used to plot graphs in report:
        h = 0.25
        k = 0.05
        n = 50
    %}

    X = (0:n)*k; Y = (0:m)*h;

    % invoking `ftcs` function program with required params
	U = ftcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("ftcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'FTCS', 'plots/q4_1.png', 'plots/q4_2.png');
	
    % invoking `btcs` function program with required params
	U = btcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("btcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'BTCS', 'plots/q4_3.png', 'plots/q4_4.png');
    
    % invoking 'crank_nicolson` function program with required params
    U = crank_nicolson(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("cn",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'Crank-Nicolson', 'plots/q4_5.png', 'plots/q4_6.png');
    
end

% ut - uxx = fun
function [y] = fun(~, ~)
	y = 0;
end

% Boundary conditions
function [y] = f(x)
	y = x.*(1-x);
end

function [y] = g1(~)
	y = 0;
end

function [y] = g2(t)
	y = t.^2;
end
