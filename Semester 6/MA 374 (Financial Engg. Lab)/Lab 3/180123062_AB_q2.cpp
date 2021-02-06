// Question 2 Lab Assignment 03
// @AB Satyaprakash, 180123062

// include all libraries
#include <bits/stdc++.h>
using namespace std;

map<pair<double, double>, double> mp;

// functions
double recursion(double n, double Smax, double S, double T, double r, double sig, double M, double u, double d, double p, double q, double dt)
{
        // if already in the map, then return
        if (mp.count({Smax, S}))
                return mp[{Smax, S}];

        // else if n==M and assign to map and return
        if (n == M)
        {
                mp[{Smax, S}] = Smax - S;
                return Smax - S;
        }

        // else do recursion
        double up = recursion(n + 1, max(Smax, S * u), S * u, T, r, sig, M, u, d, p, q, dt);
        double dn = recursion(n + 1, max(Smax, S * d), S * d, T, r, sig, M, u, d, p, q, dt);
        double pc = (exp(-r * dt)) * (p * up + q * dn);
        mp[{Smax, S}] = pc;
        return pc;
}

// code begins in main
int main()
{
        // Given initial values
        double S0 = 100, T = 1, r = 0.08, sig = 0.2;

        vector<double> M(4);
        // Given 4 values of M in question 1
        M = {5, 10, 25, 50};

        for (int i = 0; i < (int)M.size(); i++)
        {
                // evaluate dt, u, d, p and q as per formulae given in question
                double dt = T / M[i];
                double u = exp(sig * sqrt(dt) + (r - sig * sig / 2) * dt);
                double d = exp(-sig * sqrt(dt) + (r - sig * sig / 2) * dt);
                double p = (exp(r * dt) - d) / (u - d);
                double q = 1 - p;
                mp.clear();

                double optionPrice = recursion(0, S0, S0, T, r, sig, M[i], u, d, p, q, dt);
                cout << fixed << setprecision(15);
                cout << "The initial loopback option price for M = " << (int)M[i] << " is " << optionPrice << endl;
        }

        return 0;
}
