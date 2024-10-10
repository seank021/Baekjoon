import sys
input = sys.stdin.readline

num1, num2 = map(int, input().split())

def get_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    return a * b // get_gcd(a, b)

print(get_gcd(num1, num2))
print(get_lcm(num1, num2))
