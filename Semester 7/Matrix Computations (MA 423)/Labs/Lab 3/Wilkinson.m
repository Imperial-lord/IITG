function W = Wilkinson(n)
    W = (2*eye(n) - tril(ones(n)));
    W(:,n) = ones(n,1);
end