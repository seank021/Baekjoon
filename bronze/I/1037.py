import sys
input = sys.stdin.readline

N = int(input()) # N의 진짜 약수의 개수 (1과 N 제외)
divisors = list(map(int, input().split())) # N의 진짜 약수

divisors.sort()

print(divisors[0] * divisors[-1])
