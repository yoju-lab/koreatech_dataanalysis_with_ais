def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def primes_between(a, b):
    primes = []
    for num in range(a, b + 1):
        if is_prime(num):
            primes.append(num)
    return primes

