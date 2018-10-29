Interest Factor Project
Just a simple project calculating various kind of interest factors for time
value of money or cash flow analysis projects.

Assumptions:
1) All money coming in are made in the beginning of the compounding period.
2) All money going out are calculated as being made at the end of the period.

Files
iFactors.py : the file contains all the interest factors
Interest.py : the file used to test the interest factor calculations
README.md   : this file

Variable dictionary:
P:  present value
F:  future value
A:  annuity
G:  gradient (0 at the beginning of the first period)
i:  interest rate per compounding period (in %)
n:  number of compounding period

Interest factors
A) Discrete compounding, Discrete Payments
1)  [F/P, i, n] : Future given Present Factor
        F = P * iFactors.fpd(i,n)
2)  [P/F, i, n] : Present given Future Factor
        P = F * iFactors.pfd(i,n)
3)  [F/A, i, n] : Future given Annuity Factor
        F = A * iFactors.fad(i,n)
4)  [P/A, i, n] : Present given Annuity Factor
        P = A * iFactors.pad(i,n)
5)  [A/F, i, n] : Annity given Future Factor
        A = F * iFactors.afd(i,n)
6)  [A/P, i, n] : Annuity given Present Factor
        A = P * iFactors.apd(i,n)
7)  [P/G, i, n] : Present given Gradient Factor
        P = G * iFactors.pgd(i,n)
8)  [A/G, i, n] : Annuity given Gradient Factor
        A = G * iFactors.agd(i,n)

B) Continuous compounding, Discrete Payments
1)  [F/P, i, n] : Future given Present Factor
        F = P * iFactors.fpc(i,n)
2)  [P/F, i, n] : Present given Future Factor
        P = F * iFactors.pfc(i,n)
3)  [F/A, i, n] : Future given Annuity Factor
        F = A * iFactors.fac(i,n)
4)  [A/F, i, n] : Annity given Future Factor
        A = F * iFactors.afc(i,n)
5)  [P/A, i, n] : Annuity given Present Factor
        A = P * iFactors.apc(i,n)
6)  [A/P, i, n] : Annuity given Present Factor
        A = P * iFactors.apc(i,n)
7)  [A/G, i, n] : Annuity given Gradient Factor
        A = G * iFactors.agc(i,n)
