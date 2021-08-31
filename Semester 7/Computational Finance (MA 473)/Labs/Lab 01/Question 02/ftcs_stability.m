function ftcs_stability(lambda)
% ftcs_stability - function to check stability of the forward-difference (explicit) method
% @param - lambda
% @returns - none

    if(lambda > 1/2)
        fprintf('The explicit method is unstable');
    end
end

