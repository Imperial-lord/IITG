function d = mydet(A)
    % Function program to compute the determinant of A in O(n^3) flops

    [~,U,~,sign] = gepp_with_sign(A);
    d = prod(diag(U))*sign;
end