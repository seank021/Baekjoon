import sys
input = sys.stdin.readline

a, m = map(int, input().split())

# 잉여역수 a*: ax ≡ 1 (mod m)를 만족하는 x

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_inverse(a, m):
    if get_gcd(a, m) != 1:
        return -1
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
        
print(get_inverse(a, m))
