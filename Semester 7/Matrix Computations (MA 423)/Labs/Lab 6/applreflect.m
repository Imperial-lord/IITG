function B = applreflect(u,gamma,A)
%   A function program B = applreflect(u, gamma, A) to efficiently perform the
%   multiplication QA, where Q = I − γuu T .
    v = gamma*u;
    w = u'*A;
    C = v*w;
    B = A-C;
end