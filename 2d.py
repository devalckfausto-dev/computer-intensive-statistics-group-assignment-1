import numpy as np
np.random.seed(123)

N = 10000

theta = np. random.exponential(scale=1.0, size=N)

def p_tilde(theta):
    return np.exp(-theta -4*np.log(theta) - 1.5/theta**2)

def g(theta):
    return np.exp(-theta)

def h(theta):
    return theta

w_tilde = p_tilde(theta)/g(theta)

mu_NIS = np.mean(w_tilde*h(theta))/np.mean(w_tilde)

print("Estimated mean:", mu_NIS)