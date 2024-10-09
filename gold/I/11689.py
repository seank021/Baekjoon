import sys
input = sys.stdin.readline

n = int(input())

# 오일러 피 함수
# φ(n) ≡ ∣{m : 1 ≤ m ≤n, gcd(m,n) = 1}∣ (n ∈ N)
# ϕ(n)은 n과 서로소인 n 이하의 자연수의 개수

def euler_phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res -= res // i
            while n % i == 0:
                n //= i
        i += 1
    if n > 1:
        res -= res // n
    return res

print(euler_phi(n))
