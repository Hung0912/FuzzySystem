import numpy as np
import sys

#membership function

def triangular(x, a, b, c):
    return max(min((x-a)/(b-a), (c-x)/(c-b)), 0)

def trapezoid(x, a, b, c, d):
    return max(min((x-a)/(b-a), 1, (d-x)/(d-c)), 0)

def gaussian(x, mean, sigma):
    return np.exp(-np.power(x - mean, 2.) / (2 * np.power(sigma, 2.)))

def triangular2(array, a, b, c):
    result_array = []
    for x in array:
        result_array.append(max(min((x-a)/(b-a), (c-x)/(c-b)), 0))
    return result_array

def complex_fuzz(r, w):
    if 0. <= r <= 1. :
        return r * np.exp(1j * w)
    else:
        return 0

def trapezoid2(array, a, b, c, d):
    result_array = []
    for x in array:
        result_array.append(max(min((x-a)/(b-a), 1, (d-x)/(d-c)), 0))  
    return result_array

def gaussian2(array, mean, sigma):
    result_array = []
    for x in array:
        result_array.append(np.exp(-np.power(x - mean, 2.) / (2 * np.power(sigma, 2.))))  
    return result_array

def bell(x, a, b, c):
    return 1/(1+np.power(np.abs((x-c)/a),2*b))

def dil(x):
    return np.power(x, 0.5)

def con(x):
    return np.power(x, 2.0)

print(complex_fuzz(0.4, 0.1 * np.pi))