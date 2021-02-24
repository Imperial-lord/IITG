# Question 02, Lab 04
# AB Satyaprakash - 180123062

# imports ----------------------------------------------------------------------------


# functions --------------------------------------------------------------------------

def f(x):
    if(x == 1):
        return 10
    elif(x == 1.25):
        return 8
    elif(x == 1.5):
        return 7
    elif(x == 1.75):
        return 6
    else:
        return 5


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
X = [1, 1.25, 1.5, 1.75, 2]

# part (a) trapezoidal rule to approximate ∫f(x)dx from 1 to 2
print('Evaluated value of integral using (composite) Trapezoidal rule is',
      compositeTrapezoidalRule(X))

# part (b) simpson rule to approximate ∫f(x)dx from 1 to 2
print('Evaluated value of integral using (composite) Simpson rule is',
      compositeSimpsonRule(X))

# Without using composite rules.
X = [1, 2]
# part (a) trapezoidal rule to approximate ∫f(x)dx from 1 to 2
print('Evaluated value of integral using Trapezoidal (not composite) rule is',
      compositeTrapezoidalRule(X))

X = [1, 1.5, 2]  # the minimum for simpson's rule is n=2
# part (b) simpson rule to approximate ∫f(x)dx from 1 to 2
print('Evaluated value of integral using Simpson rule (not composite) is',
      compositeSimpsonRule(X))
