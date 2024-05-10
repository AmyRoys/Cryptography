from sympy import isprime

def primeFactorization(n): 
    factors = []
    i = 2
    while i * i <=n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def primes(n): 
    return isprime(n)

#print (primes(500))
print(primeFactorization(3120234567834567812345678900123456784442233321))