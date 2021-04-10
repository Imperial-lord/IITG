# MA 322, Lab Quiz
# AB Satyaprakash, 180123062
# Question 2
# imports
from math import tan, pi


# functions
def f(x):
    return tan(pi*x)-6


def secantMethod():
    x0, x1 = 0, 0.48
    for i in range(10):
        mul = (x1 - x0)/(f(x1)-f(x0))
        x2 = x1 - (f(x1)*mul)
        x0 = x1
        x1 = x2
    return x1


def bisectionMethod():
    a, b = 0, 0.48
    for i in range(10):
        c = (a+b)/2
        if(f(c)*f(b) < 0):
            a = c
        else:
            b = c
    return c


# program body
# Given f(x) = tan(πx)-6
root = 0.447431543  # (1/π) arctan 6
print('The root using 10 iterations of Bisection Method =', bisectionMethod())
print('Error using bisection method =', abs(bisectionMethod()-root))
print()
print('The root using 10 iterations of Secant Method =', secantMethod())
print('Error using secant method = ', abs(secantMethod()-root))

print('Clearly Bisection Method is better in this case because of smaller error!')
print('The reason why secant method fails is because - function tan(πx)-6 is too "wiggly" on the interval [x0,x1].')
print('The reason for this is tan(πx)-6 tends to infinity as x goes to 0.5')
