# Question 5 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
import sympy as sp
# ------------------------------------------------------------------------------
# (i) To show that both P(x) and Q(x) interpolate the data:
# f(−2) = −1, f(−1) = 3, f(0) = 1, f(1) = −1, f(2) = 3
# Given:
# P(x) = 3 − 2(x + 1) + 0(x + 1)(x) + (x + 1)(x)(x − 1)
# Q(x) = −1 + 4(x + 2) − 3(x + 2)(x + 1) + (x + 2)(x + 1)(x)
x = sp.Symbol('x')
px = 3 - 2*(x+1) + 0*(x+1)*(x) + (x+1)*(x)*(x-1)
qx = -1 + 4*(x+2) - 3*(x+2)*(x+1) + (x+2)*(x+1)*(x)

X = [-2, -1, 0, 1, 2]
F = [-1, 3, 1, -1, 3]
ok = True  # will change this to false if either P or Q does not interpolate

for i in range(len(X)):
    pval = px.subs(x, X[i])
    print('The value of P({}) = {}'.format(X[i], pval))
    if pval != F[i]:
        ok = False
print('\n')
for i in range(len(X)):
    qval = qx.subs(x, X[i])
    print('The value of Q({}) = {}'.format(X[i], qval))
    if qval != F[i]:
        ok = False

if ok == True:
    print("\nThus, both cubic polynomails P(x) and Q(x) interpolate the given data")

# (ii) Why does part (i) not violate the uniqueness property of interpolating polynomials
px = sp.expand(px)
qx = sp.expand(qx)
print('Simplifying P(x) we get', px)
print('Simplifying Q(x) we get', qx)
print('Since we can clearly see that P(x) = Q(x), this ensures that the uniqueness property of interpolating polynmials is not violated')

# Question 5 ends --------------------------------------------------------------
