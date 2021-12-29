function y = Horner(p,x)
    %   A function program to implement Horner's Rule
    %{
        Note 1: (Horner’s method) - Given p(z) = Σ nk=0 p n−k+1 z k , the Horner’s
        method uses the fact that
        p1*x^n + p2*x^n−1 + · · · + pn*x + pn+1 = pn+1 + x*(pn + · · · + x(p3 + x*(p2 + p1*x)))
        to evaluate p(z) at z = x.
    %}
    
    sz = size(x); len = length(x);
    y = zeros(sz);
    for i=1:len
        y(i) = Helper_Function(p,x(i));
    end
end

function y = Helper_Function(p, x)
    if size(p, 2) == 1
        y = p(1);
    elseif size(p, 2) == 2
        y = p(1)*x + p(2);
    else
        y = p(end) + x*Helper_Function(p(1:end-1), x);
    end
end




