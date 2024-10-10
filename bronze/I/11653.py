import sys
input = sys.stdin.readline

N = int(input())

def prime_factorization(n):
    primes = []
    for i in range(2, n):
        while n % i == 0:
            primes.append(i)
            n //= i
    if n > 1:
        primes.append(n)
    return primes

primes = prime_factorization(N)
for prime in primes:
    print(prime)
