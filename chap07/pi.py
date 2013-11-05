import math

def estimate_pi():
    c = 2*math.sqrt(2)/9801
    k = 0
    pi_guess = 0
    while abs(1/math.pi - pi_guess) > 1e-15: 
        pi_guess += c*math.factorial(4.0*k)*(1103 + 26390*k)/(math.factorial(k)**4.0*396**(4*k))
        k = k + 1
    return 1 / pi_guess

print "%.15f" %estimate_pi() #Heather taught be string formatting 