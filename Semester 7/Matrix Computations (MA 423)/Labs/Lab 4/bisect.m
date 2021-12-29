function x = bisect(p,x0,x1,tol)
    %   A function program to implement Bisection Method
    %{
        The traditional bisection method is a tool to find
        a root of a polynomial p(x) in an interval which makes repeated use of the fact
        that given a continuous function f on an interval [a, b], such that f (a) and f (b) 
        are of opposite sign, there exists at least one c ∈ (a, b) such that f (c) = 0.
    %}
    
    x_mid = x0 + (x1 - x0)/2;
    % Check for tolerance and opposite sign
    while (Horner(p,x_mid) > tol && Horner(p,x0) * Horner(p,x1) < 0)
         if Horner(p,x_mid)*Horner(p,x0) < 0 
             x1 = x_mid;
         else
             x0 = x_mid;
         end
         x_mid = x0 + (x1 - x0)/2;
    end
    x = x_mid;
end

