function [u,gamma,t]=reflect(x)
%   A MATLAB function program [u, γ, τ ] = reflect(x) to compute 
%   u ∈ Rn, and γ ∈ R, so that Qx = [−τ, 0, . . . , 0] T where τ = ±||x||2
    sign=1;
    x1=x(1);
    if x1<0
        sign=-1;
    end
    
    t=sign*norm(x,2);
    y=zeros(size(x,1),1);
    y(1)=-t;
    u=(x-y)/(x1+t);
    gamma=(t+x1)/t;
end