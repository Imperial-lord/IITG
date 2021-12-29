function [iter,lambda] = Powermethod(A,qhat,k)
    q = [];
    q = [q qhat];
    for j=1:k
        qhat = A*qhat;
        [~,i] = max(abs(qhat));
        s = qhat(i);
        qhat = qhat/s;
        q = [q qhat];
    end
    iter = q;
    lambda = s;
end