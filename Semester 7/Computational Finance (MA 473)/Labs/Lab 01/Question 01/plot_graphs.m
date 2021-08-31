function plot_graphs(X,Y,U, title_name, plot1_name, plot2_name)
% plot_graphs - function to plot grpahs inside the main function
% @param - X,Y,U, title_name, plot1_name, plot2_name
% @returns - none
    
    % line plot
    figure; plot(Y, U(end, :)); xlabel('x'); ylabel('u(x, T)'); title(title_name);
	saveas(gcf, plot1_name);
    
    % surface plot
	figure; surf(X, Y, U'); xlabel('t'); ylabel('x'); zlabel('u(t,x)'); title(title_name);
	saveas(gcf, plot2_name);
end