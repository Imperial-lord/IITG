# MA 322, Lab Quiz
# AB Satyaprakash, 180123062
# Question 3
# imports
from math import pow
import numpy as np
import matplotlib.pyplot as plt


# functions

# take the function to be x^2 (2 fixed points in R, i.e, 0 and 1)
def f(x):
    return pow(x, 2)


# program body
# we can make a quick guess that {xn} will converge to 0 and {yn} will diverge from 0
# pointing out the first 3 terms of the sequeneces
x0, y0 = 1/2, 2
x_list, y_list = [x0], [y0]
for i in range(2):
    x0 = f(x0)
    x_list.append(x0)
    y0 = f(y0)
    y_list.append(y0)
fx_list = [f(x) for x in x_list]
fy_list = [f(y) for y in y_list]

# plotting the graph of x^2 for 500 evenly spaced values
X = np.linspace(0, 25, 500)
Y = [f(x) for x in X]

plt.title('Graph of x^2 - function with 2 fixed points')
plt.plot(X, Y, label='Function f(x) = x^2')
plt.scatter(x_list, fx_list, label='Converging Sequence (xn) (x0 = 0.5)')
plt.scatter(y_list, fy_list, label='Diverging Sequence (y) (y0 = 2)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.show()
