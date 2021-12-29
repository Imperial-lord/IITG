x = linspace(1.93,2.08,151);
p = [1 -18 144 -672 2016 -4032 5376 -4608 2304 -512];
% Direct evaluation
z1 = (x - 2).^9;

% Array to store horner evaluation
z2 = [];
for i = x
    z2 = [z2; Horner(p,i)];
end

% Plotting both in the same graph
plot(x,z1);
xlabel('x'); ylabel('p(x)');
hold on
plot(x,z2);
legend('Direct method','Horner method');