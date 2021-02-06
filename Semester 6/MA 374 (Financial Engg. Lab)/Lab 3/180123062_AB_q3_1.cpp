// Question 3 Algorithm 1 Lab Assignment 03
// @AB Satyaprakash, 180123062

// include all libraries
#include <bits/stdc++.h>
using namespace std;

// functions
double recursion(double n, double K, double S, double T, double r, double sig, double M, double u, double d, double p, double q, double dt)
{

    // else if n==M and assign to map and return
    if (n == M)
        return max(S - K, 0.0);

    // else do recursion
    double up = recursion(n + 1, K, S * u, T, r, sig, M, u, d, p, q, dt);
    double dn = recursion(n + 1, K, S * d, T, r, sig, M, u, d, p, q, dt);
    double pc = (exp(-r * dt)) * (p * up + q * dn);
    return pc;
}

// code begins in main
int main()
{
    // Given initial values and taking K = 100
    double S0 = 100, K = 100, T = 1, r = 0.08, sig = 0.2;

    vector<double> M(4);
    // Can't handle values of M beyond 25 ..
    M = {5, 10, 25};

    for (int i = 0; i < (int)M.size(); i++)
    {
        // evaluate dt, u, d, p and q as per formulae given in question
        double dt = T / M[i];
        double u = exp(sig * sqrt(dt) + (r - sig * sig / 2) * dt);
        double d = exp(-sig * sqrt(dt) + (r - sig * sig / 2) * dt);
        double p = (exp(r * dt) - d) / (u - d);
        double q = 1 - p;

        double optionPrice = recursion(0, K, S0, T, r, sig, M[i], u, d, p, q, dt);
        cout << fixed << setprecision(15);
        cout << "The initial european call option price for M = " << (int)M[i] << " is " << optionPrice << endl;
    }

    return 0;
}
