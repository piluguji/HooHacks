import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm

#
# S: Price Of Stock, K: Strike Price
# Sigma: Implied Volatility, t: years till expiration
# r: interest rate
#

#Theoretical Premium
def call_value(S, K, sigma, t=0, r=0):
    with np.errstate(divide='ignore'):
        d1 = np.divide(1, sigma * np.sqrt(t)) * (np.log(S/K) + (r+sigma**2 / 2) * t)
        d2 = d1 - sigma * np.sqrt(t)
    return np.multiply(norm.cdf(d1),S) - np.multiply(norm.cdf(d2), K * np.exp(-r * t))

#Calculates the gradient
def call_vega(S, K, sigma, t=0, r=0):
    with np.errstate(divide='ignore'):
        d1 = np.divide(1, sigma * np.sqrt(t)) * (np.log(S/K) + (r+sigma**2 / 2) * t)
    return np.multiply(S, norm.pdf(d1)) * np.sqrt(t)

#Uses Newton's method to find Implied volalility from theoretical premium
def bs_iv(price, S, K, t=0, r=0, precision=1e-4, initial_guess=0.2, itr=1000, verbose=False):
    iv = initial_guess
    for _ in range(itr):
        P = call_value(S, K, iv, t, r)
        diff = price - P
        if abs(diff) < precision:
            return iv
        grad = call_vega(S, K, iv, t, r)
        iv += diff/grad     
    if verbose:
        print(f"no convergence with {itr} iterations")
    return iv

def pdf2(Krange, S, t=0, r=0):
    # x is a range of strikes
    #adds implied volatility to the dataframe and drops NAN values
    calls["iv"] = calls.apply(lambda row: bs_iv(row.midprice, S, row.strike, t, max_iter=500), axis=1)
    calls_no_na = calls.dropna()

    #Smooths out the the list
    calls_clean["iv"] = gaussian_filter1d(calls_no_na.iv, 3)

    # calls_clean = calls_clean[(calls_clean.strike > 300) & (calls_clean.strike < 375)]

    #Interpolates values 
    vol_surface = scipy.interpolate.interp1d(calls_clean.strike, calls_clean.iv, kind="cubic", fill_value="extrapolate")
    x_new = np.arange(calls_clean.strike.min(), calls_clean.strike.max(), 0.1)

    C_interp = call_value(S, x_new, vol_surface(x_new), t)
    Crange = call_value(S, Krange, vol_surface(Krange), t, r)
    
    first_deriv = np.gradient(Crange, x_new, edge_order=0)
    second_deriv = np.gradient(first_deriv, x_new, edge_order=0)

    return np.exp(r * t) * second_deriv

bs_iv()
pdf2(price, S, K, t=0, r=0, precision=1e-4, initial_guess=0.2, itr=1000, verbose=False)

