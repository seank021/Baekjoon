import sys
input = sys.stdin.readline

N, K = map(int, input().split())
MOD = 1000000007

def factorial(n):
    result = 1
    for i in range(2, n+1):
        result = (result * i) % MOD
    return result

def mod_inverse(a, mod):
    return pow(a, mod-2, mod)

def binomial_coefficient(n, k):
    num = factorial(n)
    denom = (factorial(k) * factorial(n-k)) % MOD
    return (num * mod_inverse(denom, MOD)) % MOD

print(binomial_coefficient(N, K))
