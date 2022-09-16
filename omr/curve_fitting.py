import numpy as np
from scipy.optimize import curve_fit
from scipy.stats import norm





def sigmoid(x, L ,x0, k, b):
    y = L / (1 + np.exp(-k*(x-x0)))+b
    return (y)

def fit_sigmoid(ydata):
    xdata = [1,10,20,30,50,70,100]
    p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess
    popt, pcov = curve_fit(sigmoid, xdata, ydata,p0, method='dogbox')
    y = sigmoid(xdata, *popt)
    new_x = np.linspace(0,100,50)
    new_y = sigmoid(new_x, *popt)
    return new_y

def gauss(x, mu, sigma, A):
    return A*np.exp(-(x-mu)**2/2/sigma**2)

def bimodal(x, mu1, sigma1, A1, mu2, sigma2, A2):
    return gauss(x,mu1,sigma1,A1)+gauss(x,mu2,sigma2,A2)

def straight_line(x, A, B): # this is your 'straight line' y=f(x)
    return np.multiply(A,x) + B

# popt, pcov = curve_fit(f, x, y) # your data x, y to fit

def fit_straight_line(ydata):
    xdata = [1,10,20,30,50,70,100]
#     p0 = [max(ydata), np.median(xdata),1,min(ydata)] # this is an mandatory initial guess
    popt, pcov = curve_fit(straight_line, xdata, ydata)
    y = straight_line(xdata, popt[0],popt[1])
    new_x = np.linspace(0,100,50)
    new_y = straight_line(new_x, popt[0],popt[1])
    return new_y

def bimodal_2(x,mu1,sigma1,mu2,sigma2, p, A):
    return p * A * norm.pdf(x,mu1,sigma1)+ (1-p) * A * norm.pdf(x,mu2,sigma2)
