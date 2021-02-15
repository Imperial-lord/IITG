# Question 1 Lab 03
# AB Satyaprakash (180123062)

# imports ----------------------------------------------------------------------
import numpy as np
# ------------------------------------------------------------------------------
# functions --------------------------------------------------------------------


def forwardDiff(fArray):
    sz = len(fArray)
    fdArray = [fArray]
    for i in range(1, sz):
        temp = []
        for j in range(sz-i):
            temp.append(fdArray[i-1][j+1]-fdArray[i-1][j])
        fdArray.append(temp)
    return fdArray


def newtonFDPoly(fArray, xArray):
    x0, x1 = xArray[0], xArray[1]
    h = x1-x0
    u = np.array([1/h, -x0/h])
    fdArray = forwardDiff(fArray)
    sz = len(fArray)
    px = np.array([0])

    for i in range(sz):
        term = np.array([1])
        for j in range(i):
            term = np.polymul(term, np.polyadd(u, np.array([-j])))
            term = term/(j+1)
        term = term*fdArray[i][0]
        px = np.polyadd(px, term)
    return px


# ------------------------------------------------------------------------------
# (i) f(0.43) if f(0) = 1, f(0.25) = 1.64872, f(0.5) = 2.71828, f(0.75) = 4.48169
print('Part (i)-----------------------------------------------------------------\n')
X = [0, 0.25, 0.5, 0.75]
F = [1, 1.64872, 2.71828, 4.48169]
val = 0.43  # since we need to approximate f(0.43)
# (A) Degree 1:

xArray = [X[1], X[2]]
fArray = [F[1], F[2]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 1 using nodes: {}, {} is {}".format(
    xArray[0], xArray[1], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (B) Degree 2:

xArray = [X[1], X[2], X[3]]
fArray = [F[1], F[2], F[3]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 2 using nodes: {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (C) Degree 3:
xArray = [X[0], X[1], X[2], X[3]]
fArray = [F[0], F[1], F[2], F[3]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 3 using nodes: {}, {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], xArray[3], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))


# (ii) f(0.18) if f(0.1) = −0.29004986, f(0.2) = −0.56079734, f(0.3) = −0.81401972, f(0.4) = −1.0526302
print('\nPart (ii)--------------------------------------------------------------\n')
X = [0.1, 0.2, 0.3, 0.4]
F = [-0.29004986, -0.56079734, -0.81401972, -1.0526302]
val = 0.18  # since we need to approximate f(0.18)
# (A) Degree 1:

xArray = [X[0], X[1]]
fArray = [F[0], F[1]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 1 using nodes: {}, {} is {}".format(
    xArray[0], xArray[1], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (B) Degree 2:
xArray = [X[0], X[1], X[2]]
fArray = [F[0], F[1], F[2]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 2 using nodes: {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (C) Degree 3:
xArray = [X[0], X[1], X[2], X[3]]
fArray = [F[0], F[1], F[2], F[3]]
px = newtonFDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 3 using nodes: {}, {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], xArray[3], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))


# Question 1 ends --------------------------------------------------------------
