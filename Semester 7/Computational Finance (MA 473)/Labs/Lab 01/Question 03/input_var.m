function [h,k,n] = input_var()
% input_var - function to input the variables h, k and n
% @param - none
% @returns - h, k, n

    h = input('Enter spatial step-size: ');
    k = input('Enter time step-size: ');
    n = input('Enter number of time-levels: ');
end

