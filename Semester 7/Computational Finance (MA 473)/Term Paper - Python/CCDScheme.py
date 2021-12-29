import numpy as np
from compositeBoole import compositeBool
from findUInitial import findUInitial
from findVWInitial import findVWInitial
from g import g


def findCCDScheme(u_n, v_n, w_n, N, M, b, T, r, lambda_val, sigma, nu, eta):
    h = 2*b/M
    k = T/N
    x = np.arange(-b, b+h, h)

    B = np.zeros(3*M+3)
    A = np.zeros((3*M+3, 3*M+3))

    for i in range(0, 3*M-3):
        i1 = int((i+3)/3)
        if i % 3 == 2:
            gamma = compositeBool(u_n, M, b, r, lambda_val, sigma, nu, eta, i1)
            B[i] = u_n[i1] + k*sigma*sigma/4*w_n[i1] + k*lambda_val*gamma/2
        elif i % 3 == 0:
            B[i] = -v_n[i1]
        else:
            B[i] = 0

    gamma = compositeBool(u_n, M, b, r, lambda_val, sigma, nu, eta, 0)
    B[3*M-3] = u_n[0] + k*sigma*sigma/4*w_n[0] + k*lambda_val*gamma/2
    gamma = compositeBool(u_n, M, b, r, lambda_val, sigma, nu, eta, M)
    B[3*M-2] = u_n[M] + k*sigma*sigma/4*w_n[M] + k*lambda_val*gamma/2

    for i in range(0, 3*M-3):
        i1 = int((i+3)/3)
        if i % 3 == 2:
            A[i][i1] = 1
            A[i][2*M+2+i1] = -k*sigma*sigma/4
            A[i][0] += (2*h/45) * (-k*lambda_val/2) * 7 * \
                g(-b-x[i1], r, lambda_val, sigma, nu, eta)
            A[i][M] += (2*h/45) * (-k*lambda_val/2) * 7 * \
                g(b-x[i1], r, lambda_val, sigma, nu, eta)

            for l in range(0, int(M/4)-1):
                A[i][4*l+1] += (2*h/45) * (-k*lambda_val/2) * 32 * \
                    g(x[4*l+1]-x[i1], r, lambda_val, sigma, nu, eta)
                A[i][4*l+2] += (2*h/45) * (-k*lambda_val/2) * 12 * \
                    g(x[4*l+2]-x[i1], r, lambda_val, sigma, nu, eta)
                A[i][4*l+3] += (2*h/45) * (-k*lambda_val/2) * 32 * \
                    g(x[4*l+3]-x[i1], r, lambda_val, sigma, nu, eta)
                A[i][4*l+4] += (2*h/45) * (-k*lambda_val/2) * 14 * \
                    g(x[4*l+4]-x[i1], r, lambda_val, sigma, nu, eta)

            A[i][M-3] += (2*h/45) * (-k*lambda_val/2) * 32 * \
                g(x[M-3]-x[i1], r, lambda_val, sigma, nu, eta)
            A[i][M-2] += (2*h/45) * (-k*lambda_val/2) * 12 * \
                g(x[M-2]-x[i1], r, lambda_val, sigma, nu, eta)
            A[i][M-1] += (2*h/45) * (-k*lambda_val/2) * 32 * \
                g(x[M-1]-x[i1], r, lambda_val, sigma, nu, eta)

        elif i % 3 == 0:
            A[i][i1-1] = (15/(16*h))
            A[i][i1+1] = -(15/(16*h))
            A[i][M+1+i1-1] = 7/16
            A[i][M+1+i1+1] = 7/16
            A[i][2*M+2+i1-1] = h/16
            A[i][2*M+2+i1+1] = -h/16

        else:
            A[i][i1-1] = 3/(h*h)
            A[i][i1] = -6/(h*h)
            A[i][i1+1] = 3/(h*h)
            A[i][M+1+i1-1] = 9/(8*h)
            A[i][M+1+i1+1] = -9/(8*h)
            A[i][2*M+2+i1-1] = 1/8
            A[i][2*M+2+i1] = -1
            A[i][2*M+2+i1+1] = 1/8

    A[3*M-3][0] = 1
    A[3*M-3][2*M+2] = -k*sigma*sigma/4
    A[3*M-3][0] += (2*h/45) * (-k*lambda_val/2) * 7 * \
        g(-b-x[0], r, lambda_val, sigma, nu, eta)
    A[3*M-3][M] += (2*h/45) * (-k*lambda_val/2) * 7 * \
        g(b-x[0], r, lambda_val, sigma, nu, eta)

    for l in range(0, int(M/4)-1):
        A[3*M-3][4*l+1] += (2*h/45) * (-k*lambda_val/2) * \
            32 * g(x[4*l+1]-x[0], r, lambda_val, sigma, nu, eta)
        A[3*M-3][4*l+2] += (2*h/45) * (-k*lambda_val/2) * \
            12 * g(x[4*l+2]-x[0], r, lambda_val, sigma, nu, eta)
        A[3*M-3][4*l+3] += (2*h/45) * (-k*lambda_val/2) * \
            32 * g(x[4*l+3]-x[0], r, lambda_val, sigma, nu, eta)
        A[3*M-3][4*l+4] += (2*h/45) * (-k*lambda_val/2) * \
            14 * g(x[4*l+4]-x[0], r, lambda_val, sigma, nu, eta)

    A[3*M-3][M-3] += (2*h/45) * (-k*lambda_val/2) * 32 * \
        g(x[M-3]-x[0], r, lambda_val, sigma, nu, eta)
    A[3*M-3][M-2] += (2*h/45) * (-k*lambda_val/2) * 12 * \
        g(x[M-2]-x[0], r, lambda_val, sigma, nu, eta)
    A[3*M-3][M-1] += (2*h/45) * (-k*lambda_val/2) * 32 * \
        g(x[M-1]-x[0], r, lambda_val, sigma, nu, eta)

    # FOR j=M

    A[3*M-2][M] = 1
    A[3*M-2][2*M+2+M] = -k*sigma*sigma/4
    A[3*M-2][0] += (2*h/45) * (-k*lambda_val/2) * 7 * \
        g(-b-x[M], r, lambda_val, sigma, nu, eta)
    A[3*M-2][M] += (2*h/45) * (-k*lambda_val/2) * 7 * \
        g(b-x[M], r, lambda_val, sigma, nu, eta)

    for l in range(0, int(M/4)-1):
        A[3*M-2][4*l+1] += (2*h/45) * (-k*lambda_val/2) * \
            32 * g(x[4*l+1]-x[M], r, lambda_val, sigma, nu, eta)
        A[3*M-2][4*l+2] += (2*h/45) * (-k*lambda_val/2) * \
            12 * g(x[4*l+2]-x[M], r, lambda_val, sigma, nu, eta)
        A[3*M-2][4*l+3] += (2*h/45) * (-k*lambda_val/2) * \
            32 * g(x[4*l+3]-x[M], r, lambda_val, sigma, nu, eta)
        A[3*M-2][4*l+4] += (2*h/45) * (-k*lambda_val/2) * \
            14 * g(x[4*l+4]-x[M], r, lambda_val, sigma, nu, eta)

    A[3*M-2][M-3] += (2*h/45) * (-k*lambda_val/2) * 32 * \
        g(x[M-3]-x[M], r, lambda_val, sigma, nu, eta)
    A[3*M-2][M-2] += (2*h/45) * (-k*lambda_val/2) * 12 * \
        g(x[M-2]-x[M], r, lambda_val, sigma, nu, eta)
    A[3*M-2][M-1] += (2*h/45) * (-k*lambda_val/2) * 32 * \
        g(x[M-1]-x[M], r, lambda_val, sigma, nu, eta)

    A[3*M-1][0] = 31/h
    A[3*M-1][1] = -32/h
    A[3*M-1][2] = 1/h
    A[3*M-1][M+1] = 14
    A[3*M-1][M+1+1] = 16
    A[3*M-1][2*M+2] = 2*h
    A[3*M-1][2*M+2+1] = -4*h

    A[3*M][M] = -31/h
    A[3*M][M-1] = 32/h
    A[3*M][M-2] = -1/h
    A[3*M][M+1+M] = 14
    A[3*M][M+1+M-1] = 16
    A[3*M][2*M+2+M] = -2*h
    A[3*M][2*M+2+M-1] = 4*h

    A[3*M+1][0] = 7/(2*h)
    A[3*M+1][1] = -8/(2*h)
    A[3*M+1][2] = 1/(2*h)
    A[3*M+1][M+1] = 1
    A[3*M+1][M+1+1] = 2
    A[3*M+1][2*M+2+1] = -h

    A[3*M+2][M] = -7/(2*h)
    A[3*M+2][M-1] = 8/(2*h)
    A[3*M+2][M-2] = -1/(2*h)
    A[3*M+2][M+1+M] = 1
    A[3*M+2][M+1+M-1] = 2
    A[3*M+2][2*M+2+M-1] = h

    X = np.matmul(np.linalg.inv(A), B)

    u_n1 = X[0:M+1]
    v_n1 = X[M+1:2*M+2]
    w_n1 = X[2*M+2:]

    print(np.linalg.norm(np.matmul(A, X) - B))

    return u_n1, v_n1, w_n1


u_n = findUInitial(1.5, 3/128, 100, -0.9, 0.45, 0.05, 0.15, 0.1, 'call')
v_n, w_n = findVWInitial(u_n, 3/128, 128)

for i in range(0, 25):
    u_n, v_n, w_n = findCCDScheme(
        u_n, v_n, w_n, 25, 128, 1.5, 0.25, 0.05, 0.1, 0.15, -0.9, 0.45)


# print(u_n[60])
