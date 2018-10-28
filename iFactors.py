"""
FINANCIAL FUNCTIONS to help time value of money calculation
interest factors
Assuming all money comes in at the beginning of the period and
all payout are done at the end of the period
common variables:
p   :present value
f   :future value
a   :annuity (regular cash flow per period over the duration)
g   :graduation
i   :interest per compounding period in %
apr :annual percentage rate; default 12 compounding period/ year
     unless explicitly specified
n   : number of compounding period
"""

import math

def fpd(i,n):
    # F given P factor with interest i over n periods discrete compounding
    return ((1+i/100.00)**n)

def pfd(i,n):
    # present given future factor discrete compounding
    return (1.0/fpd(i,n))

def fad(i,n):
    # future given annuity factor discrete compounding
    return ((fpd(i,n)-1.0)*100/i)

def pad(i,n):
    #present given annuity factor discrete compounding
    return (pfd(i,n)*fad(i,n))

def afd(i,n):
    # annuity given future factor discrete compounding
    return (1/fad(i,n))

def apd(i,n):
    # annuity given present value factor descret compounding
    return(1/pad(i,n))

def pgd(i,n):
    # present given gradient factors discrete compounding
    fp = fpd(i,n)
    pg = 100.00/i/fpd(i,n)*(fad(i,n)-n)
    return (pg)

def agd(i,n):
    # annuity given gradient factor discrete compounding
    ag = 100.00/i - n/(fpd(i,n)-1.0)
    return (ag)

"""
CONTINUOUS COMPOUNDING; Discrete Payments;
"""

def fpc(r,n):
    return (math.exp(r*n/100.0))

def pfc(r,n):
    return (1.0/fpc(r,n))

def fac(r,n):
    fa = (fpc(r,n)-1.0)/(math.exp(r/100.0)-1.0)
    return (fa)

def afc(r,n):
    return (1.0/fac(r,n))

def pac(r,n):
    return(fac(r,n)/fpc(r,n))

def apc(r,n):
    return (1.0/pac(r,n))

def agc(r,n):
    ag = 1.0/(math.exp(r/100.0)-1.0)-n/(math.exp(r*n/100.0)-1.0)
    return (ag)
