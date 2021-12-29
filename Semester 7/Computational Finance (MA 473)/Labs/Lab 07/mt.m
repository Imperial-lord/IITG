function mt(e)
    dx=0.1;dt=0.01;
    T=0.2;K=100;sig=0.25;r=0.05;
    a = @(x) sig^2*x^2/(2*dx^2);
    b = @(x) (1-r*x)/(2*dx);
    Rmax=1;
    t=0:dt:0.2;
    R=0:dx:Rmax;
    m=length(R);
    n=length(t);
    A=eye(m,m);B=A;
    for i=2:m-1
        A(i,i)=1/dt-2*a(R(i))*e;
        A(i,i-1)=e*(a(R(i))-b(R(i)));
        A(i,i+1)=e*(a(R(i))+b(R(i)));
        B(i,i)=1/dt+2*a(R(i))*(1-e);
        B(i,i-1)=-(1-e)*(a(R(i))-b(R(i)));
        B(i,i+1)=-(1-e)*(a(R(i))+b(R(i)));
    end
    A(2:end-1,:)=A(2:end-1,:)*dt;
    B(2:end-1,:)=B(2:end-1,:)*dt;
    B(1,1)=1+3*dt/(2*dx);
    B(1,2)=-2*dt/dx;
    B(1,3)=dt/(2*dx);
    U=zeros(m,n);
    U(:,n)=max(1-R/T,0);
    U(m,:)=0;
    for i=n-1:-1:1
        bb=A*U(:,i+1);
        U(:,i)=B\(bb);
    end
    surf(R,t,U');
end
