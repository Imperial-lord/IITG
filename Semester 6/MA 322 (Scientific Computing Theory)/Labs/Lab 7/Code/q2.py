# Question 02, Lab 07
# AB Satyaprakash, 180123062

# imports

# functions
def f(t, y):
    return -y+t+1


def RungeKutta2(t, y, h):
    return y + h*f(t+h/2, y+h*f(t, y)/2)


def ModifiedEuler(t, y, h):
    return y + h*(f(t, y) + f(t+h, y+h*f(t, y)))/2


# program body
hList = [0.2, 0.1, 0.05, 0.01]

for h in hList:
    t, y1, y2 = 0, 1, 1
    while t < 0.2:
        y1 = RungeKutta2(t, y1, h)
        y2 = ModifiedEuler(t, y2, h)
        t += h
    print('Runge-Kutta Method of Order 2 with h = {} gives y(0.2) = {}'.format(h, y1))
    print('Modified Euler Method h = {} gives y(0.2) = {}'.format(h, y2))
    print('The difference between the two values = {}\n'.format(abs(y1-y2)))
