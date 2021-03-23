# Question 3, Lab 07
# AB Satyaprakash, 180123062

# imports
import numpy as np

# functions


def F(t, part):
    if part == 'a':
        return np.sqrt(t**2 + 6 + 2*t) - 1
    else:
        return (4+np.cos(2)-np.cos(2*t))/(2*(t**2))


def f(t, y, part):
    if part == 'a':
        return (t+1)/(y+1)
    else:
        return (np.sin(2*t) - 2*t*y)/(t**2)


def ModEuler(t, y, h, part):
    k1 = f(t, y, part)
    k2 = k1 + f(t+h, y+h*k1, part)
    return y + h*k2/2

# program body
# part (a)


h, t, y = 0.5, 1, 2
while t <= 2:
    print('For part (a) y({}) is approximated as {}'.format(t, y))
    print('Actual value of y({}) is given by {}\n'.format(t, F(t, 'a')))
    y = ModEuler(t, y, h, 'a')
    t += h

print('----------------------------------------------------------------')


# part (b)
h, t, y = 0.25, 1, 2
while t <= 2:
    print('For part (b) y({}) is approximated as {}'.format(t, y))
    print('Actual value of y({}) is given by {}\n'.format(t, F(t, 'b')))
    y = ModEuler(t, y, h, 'b')
    t += h
