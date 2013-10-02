def is_power(a, b):
    if a % b != 0:
        return False
    if a / b == 1:
        return True
    return is_power(a/b, b)

#print is_power(81, 3)

def gcd(a, b):
    if gcd(a, 0) == a:
        return a
    if gcd(a, b) == gdc(b, a % b):
        return b

print gcd(20, 8)