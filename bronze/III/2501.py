import sys
input = sys.stdin.readline

N, K = map(int, input().split())

def get_divisor(N):
    divisor = []
    for i in range(1, N+1):
        if N % i == 0:
            divisor.append(i)
    return divisor

divisor = get_divisor(N)

if len(divisor) < K:
    print(0)
else:
    print(divisor[K-1])
