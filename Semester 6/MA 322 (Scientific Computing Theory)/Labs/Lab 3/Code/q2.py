# Question 2 Lab 03
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


def newtonBDPoly(fArray, xArray):
    sz = len(fArray)
    xn, xn_1 = xArray[sz-1], xArray[sz-2]
    h = xn-xn_1
    # print(h)
    v = np.array([1/h, -xn/h])
    # print(v)
    fdArray = forwardDiff(fArray)
    # print(fdArray)
    px = np.array([0])

    for i in range(sz):
        term = np.array([1])
        for j in range(i):
            term = np.polymul(term, np.polyadd(v, np.array([j])))
            term = term/(j+1)
        term = term*fdArray[i][sz-i-1]
        px = np.polyadd(px, term)
    return px


# ------------------------------------------------------------------------------
# (i) f(−1/3) if f(−0.75) = −0.07181250, f(−0.5) = −0.02475000, f(−0.25) = 0.33493750, f(0) = 1.10100000
print('Part (i)-----------------------------------------------------------------\n')
X = [-0.75, -0.5, -0.25, 0]
F = [-0.07181250, -0.02475000, 0.33493750, 1.10100000]
val = -1/3  # since we need to approximate f(1/3)
# (A) Degree 1:

xArray = [X[1], X[2]]
fArray = [F[1], F[2]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 1 using nodes: {}, {} is {}".format(
    xArray[0], xArray[1], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (B) Degree 2:

xArray = [X[0], X[1], X[2]]
fArray = [F[0], F[1], F[2]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 2 using nodes: {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (C) Degree 3:
xArray = [X[0], X[1], X[2], X[3]]
fArray = [F[0], F[1], F[2], F[3]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 3 using nodes: {}, {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], xArray[3], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))


# (ii) f(0.25) if f(0.1) = −0.62049958 , f(0.2) = −0.28398668 , f(0.3) = 0.00660095, f(0.4) = 0.24842440
print('\nPart (ii)--------------------------------------------------------------\n')
X = [0.1, 0.2, 0.3, 0.4]
F = [-0.62049958, -0.28398668, 0.00660095, 0.24842440]
val = 0.25  # since we need to approximate f(0.25)
# (A) Degree 1:

xArray = [X[1], X[2]]
fArray = [F[1], F[2]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 1 using nodes: {}, {} is {}".format(
    xArray[0], xArray[1], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (B) Degree 2:
xArray = [X[0], X[1], X[2]]
fArray = [F[0], F[1], F[2]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 2 using nodes: {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))

print('\n')

# (C) Degree 3:
xArray = [X[0], X[1], X[2], X[3]]
fArray = [F[0], F[1], F[2], F[3]]
px = newtonBDPoly(fArray, xArray)
print("Newton's interpolating polynomial of degree 3 using nodes: {}, {}, {}, {} is \n{}".format(
    xArray[0], xArray[1], xArray[2], xArray[3], np.poly1d(px)))
print("Approximated value of f({}) using the above is {}".format(val, np.polyval(px, val)))


# Question 2 ends --------------------------------------------------------------
