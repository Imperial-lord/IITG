function main
    [h,k,n] = input_var();
    m = 1/h; 
    %{
        The input values used to plot graphs in report:
        h = 0.025
        k = 0.05
        n = 3
    %}

    X = (0:n)*k; Y = (0:m)*h;

    % invoking `ftcs` function program with required params
	U = ftcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("ftcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'FTCS', 'plots/q1_1.png', 'plots/q1_2.png');
	
    % invoking `btcs` function program with required params
	U = btcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("btcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'BTCS', 'plots/q1_3.png', 'plots/q1_4.png');
    
    % invoking 'crank_nicolson` function program with required params
    U = crank_nicolson(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("cn",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'Crank-Nicolson', 'plots/q1_5.png', 'plots/q1_6.png');
    
end

% ut - uxx = fun
function [y] = fun(x, t)
    y = sin(2*pi*x).*sin(4*pi*t);
end

% Boundary conditions
function [y] = f(~)
	y = 0;
end

function [y] = g1(~)
	y = 0;
end

function [y] = g2(~)
	y = 0;
end
