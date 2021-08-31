function main
    [h,k,n] = input_var();
    m = 1/h; 
        
    %{
        The input values used to plot graphs in report:
        h = 0.1
        k = 0.005
        n = 20
    %}
    
    X = (0:n)*k; Y = (0:m)*h;

    % invoking `ftcs` function program with required params
	U = ftcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("ftcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'FTCS', 'plots/q3_1.png', 'plots/q3_2.png');
	
    % invoking `btcs` function program with required params
	U = btcs(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("btcs",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'BTCS', 'plots/q3_3.png', 'plots/q3_4.png');
    
    % invoking 'crank_nicolson` function program with required params
    U = crank_nicolson(h, k, m, n, @fun, @f, @g1, @g2);
    error_table("cn",@fun, @f, @g1, @g2);
    plot_graphs(X,Y,U, 'Crank-Nicolson', 'plots/q3_5.png', 'plots/q3_6.png');
    
end

% ut - uxx = fun
function [y] = fun(~, ~)
	y = 0;
end

% Boundary conditions
function [y] = f(x)
	y = cos(pi*x/2);
end

function [y] = g1(~)
	y = 0;
end

function [y] = g2(~)
	y = 0;
end
