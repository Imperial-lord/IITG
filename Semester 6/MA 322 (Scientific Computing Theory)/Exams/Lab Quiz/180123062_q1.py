# MA 322, Lab Quiz
# AB Satyaprakash, 180123062
# Question 1
# imports
from math import log, pow, ceil, sqrt


# functions
def f(x):
    return sqrt(x)-1.1

def g(x):
    return (x+1.21)/2

def noOfIterations(a, b, epsilon):
    return ceil((log(b-a)-log(epsilon))/log(2))


# program body
# Given f(x) = sqrt(x)-1.1
a0, b0, epsilon0 = 0, 2, pow(10, -8)
root = 1.1**2
print('The root of this equation in [0,2] will be', round(root,2))

# part A
itr = 0
a = a0
b = b0
while(True):
    itr += 1
    c = (a+b)/2
    if(abs(c-root) < epsilon0):
        break
    if(f(c)*f(b) < 0):
        a = c
    else:
        b = c

print('Bisection root = {} & No of iterations = {}'.format(c, itr))
print('Expected iteration (to nearest integer) count based on convergence analysis is',
      noOfIterations(a0, b0, epsilon0))
print()

# part B
print('For this part we make use of g(x) = (x+1.21)/2. Note that this also satifies the contraction-mapping theorem')
itr = 0
x0 = 0
while(True):
    itr+=1
    x1 = g(x0)
    if(abs(x1-root)<epsilon0):
        break
    x0 = x1

print('Fixed point iteration root = {} & No of iterations = {}'.format(x1,itr))