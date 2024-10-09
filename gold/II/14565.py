import sys
input = sys.stdin.readline

N, A = map(int, input().split())

def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return d, x, y

def find_add_inverse(a, n):
    if (n - a) < 0:
        return n - a + n
    return n - a

def find_mul_inverse(a, n):
    d, x, y = extended_gcd(a, n)
    if d != 1:
        return -1
    return x % n

add_inverse = find_add_inverse(A, N)
mul_inverse = find_mul_inverse(A, N)

print(add_inverse, mul_inverse)
