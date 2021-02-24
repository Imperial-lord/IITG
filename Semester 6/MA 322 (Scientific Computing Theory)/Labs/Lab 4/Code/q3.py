# Question 03, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------


# functions --------------------------------------------------------------------------


def f(t):
    return 1/(10*(t**2)-2*t+1)


def compositeTrapezoidalRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = len(X)
    h = (b-a)/(n-1)
    for i in range(len(X)):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)/2
        else:
            sum += f(x)
    return (h*sum)


def compositeSimpsonRule(X):
    sum = 0
    a, b = X[0], X[-1]
    n = len(X)
    h = (b-a)/(n-1)
    for i in range(len(X)):
        x = X[i]
        if(i == 0 or i == n-1):
            sum += f(x)
        else:
            if(i % 2 == 0):
                sum += 2*f(x)
            else:
                sum += 4*f(x)
    return (h*sum)/3


# program body
# To evaluate integral of 1/(x^2+9) from 0 to ∞, we make a change of variables - t = 1/(1+x).
# Corresponding change of limits and integrand => evaluate 1/(10t^2-2t+1) from 0 to 1.
X = [0, 0.25, 0.50, 0.75, 1]  # since n = 4

# Composite simpson rule to approximate improper integral
print('Evaluated value of integral using composite Simpson rule is',
      compositeSimpsonRule(X))
# Composite trapezoidal rule to approximate improper integral
print('Evaluated value of integral using composite Trapezoidal rule is',
      compositeTrapezoidalRule(X))
