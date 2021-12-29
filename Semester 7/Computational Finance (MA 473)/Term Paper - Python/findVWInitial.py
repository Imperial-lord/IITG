import numpy as np
from findUInitial import findUInitial


def findVWInitial(u, h, M):
    A = np.zeros((2*M+2, 2*M+2))
    b = np.zeros((2*M+2))

    for i in range(0, 2*M-2):
        i1 = int((i+2)/2)
        if i % 2 == 1:
            b[i] = 15/(16*h)*(u[i1+1]-u[i1-1])
        else:
            b[i] = 3/(h*h)*(u[i1+1]-2*u[i1]+u[i1-1])

    b[2*M-2] = (-1/h)*(31*u[0]-32*u[1]+u[2])
    b[2*M-1] = (1/h)*(31*u[M]-32*u[M-1]+u[M-2])
    b[2*M] = (-1/(2*h))*(7*u[0]-8*u[1]+u[2])
    b[2*M+1] = (1/(2*h))*(7*u[M]-8*u[M-1]+u[M-2])

    for i in range(0, 2*M-2):
        i1 = int((i+2)/2)
        if i % 2 == 1:
            A[i][i1-1] = 7/16
            A[i][i1+1] = 7/16
            A[i][i1] = 1
            A[i][M+i1] = h/16
            A[i][M+i1+2] = -h/16
        else:
            A[i][i1-1] = -9/(8*h)
            A[i][i1+1] = 9/(8*h)
            A[i][M+i1] = -1/8
            A[i][M+i1+1] = 1
            A[i][M+i1+2] = -1/8

    A[2*M-2][0] = 14
    A[2*M-2][1] = 16
    A[2*M-2][M+1] = 2*h
    A[2*M-2][M+2] = -4*h

    A[2*M-1][M] = 14
    A[2*M-1][M-1] = 16
    A[2*M-1][2*M+1] = -2*h
    A[2*M-1][2*M] = 4*h

    A[2*M][0] = 1
    A[2*M][1] = 2
    A[2*M][M+1] = -h
    A[2*M][M+2] = 0

    A[2*M+1][M] = 1
    A[2*M+1][M-1] = 2
    A[2*M+1][2*M+1] = 0
    A[2*M+1][2*M] = h

    x = np.matmul(np.linalg.inv(A), b)
    v = x[0:M+1]
    w = x[M+1:]

    return v, w


# u = findUInitial(1.5, 3/128, 100, -0.9, 0.45, 0.05, 0.15, 0.1, 'call')
# findVWInitial(u, 3/128, 128)
