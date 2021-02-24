# Question 01, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------
from sympy.abc import x
from sympy import cos, exp, pi, evalf, simplify

# functions --------------------------------------------------------------------------


def midpointRule(f, a, b):
    return ((b-a)*f.subs(x, (b-a)/2)).evalf()


def trapezoidalRule(f, a, b):
    return (((b-a)/2)*(f.subs(x, a)+f.subs(x, b))).evalf()


def simpsonRule(f, a, b):
    return (((b-a)/6)*(f.subs(x, a)+4*f.subs(x, (a+b)/2)+f.subs(x, b))).evalf()


# program body
# part (a) I = integrate cosx/(1+cos^2x) from 0 to π/2 -- exact value ≈ 0.623225
f = cos(x)/(1 + cos(x)**2)
a, b = 0, pi/2

print('To integrate {} from {} to {}'.format(simplify(f), a, b))
print('Evaluated value of integral using Midpoint rule is', midpointRule(f, a, b))
print('Evaluated value of integral using Trapezoidal rule is',
      trapezoidalRule(f, a, b))
print('Evaluated value of integral using Simpson rule is', simpsonRule(f, a, b))
print('Exact value ≈ 0.623225\n')


# part (b) I = integrate 1/(5+4cosx) from 0 to π -- exact value ≈ 1.047198
f = 1/(5 + 4*cos(x))
a, b = 0, pi

print('To integrate {} from {} to {}'.format(simplify(f), a, b))
print('Evaluated value of integral using Midpoint rule is', midpointRule(f, a, b))
print('Evaluated value of integral using Trapezoidal rule is',
      trapezoidalRule(f, a, b))
print('Evaluated value of integral using Simpson rule is', simpsonRule(f, a, b))
print('Exact value ≈ 1.047198\n')

# part (c) I = integrate exp(-x^2) from 0 to 1 -- exact value ≈ 0.746824
f = exp(-x**2)
a, b = 0, 1

print('To integrate {} from {} to {}'.format(simplify(f), a, b))
print('Evaluated value of integral using Midpoint rule is', midpointRule(f, a, b))
print('Evaluated value of integral using Trapezoidal rule is',
      trapezoidalRule(f, a, b))
print('Evaluated value of integral using Simpson rule is', simpsonRule(f, a, b))
print('Exact value ≈ 0.746824\n')
