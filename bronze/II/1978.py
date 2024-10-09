import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split())) # N numbers

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

cnt = 0
for number in numbers:
    if is_prime(number):
        cnt += 1

print(cnt)
