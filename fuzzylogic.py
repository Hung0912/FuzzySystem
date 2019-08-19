import numpy as np
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