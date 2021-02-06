// Question 3 Algorithm 2 Lab Assignment 03
// @AB Satyaprakash, 180123062

// include all libraries
#include <bits/stdc++.h>
using namespace std;

map<pair<double, double>, double> mp;

// functions
double recursion(double n, double K, double S, double T, double r, double sig, double M, double u, double d, double p, double q, double dt, int upCnt)
{
    // if already in the map, then return
    if (mp.count({n, upCnt}))
        return mp[{n, upCnt}];

    // else if n==M and assign to map and return
    if (n == M)
    {
        mp[{n, upCnt}] = max(S - K, 0.0);
        return max(S - K, 0.0);
    }

    // else do recursion
    double up = recursion(n + 1, K, S * u, T, r, sig, M, u, d, p, q, dt, upCnt + 1);
    double dn = recursion(n + 1, K, S * d, T, r, sig, M, u, d, p, q, dt, upCnt);
    double pc = (exp(-r * dt)) * (p * up + q * dn);
    mp[{n, upCnt}] = pc;
    return pc;
}

// code begins in main
int main()
{
    // Given initial values and taking K = 100
    double S0 = 100, K = 100, T = 1, r = 0.08, sig = 0.2;

    vector<double> M(4);
    // Can handle M values upto 1000
    M = {5, 10, 25, 50, 100, 500, 1000};

    for (int i = 0; i < (int)M.size(); i++)
    {
        // evaluate dt, u, d, p and q as per formulae given in question
        double dt = T / M[i];
        double u = exp(sig * sqrt(dt) + (r - sig * sig / 2) * dt);
        double d = exp(-sig * sqrt(dt) + (r - sig * sig / 2) * dt);
        double p = (exp(r * dt) - d) / (u - d);
        double q = 1 - p;
        mp.clear();

        double optionPrice = recursion(0, K, S0, T, r, sig, M[i], u, d, p, q, dt, 0);
        cout << fixed << setprecision(15);
        cout << "The initial european call option price for M = " << (int)M[i] << " is " << optionPrice << endl;
    }

    return 0;
}
