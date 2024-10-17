import sys
input = sys.stdin.readline

T = int(input())
MOD = 1000000007

MAX_N = 2500
catalan = [0] * (MAX_N + 1)
catalan[0] = 1

# 카탈란 수 계산
for n in range(1, MAX_N + 1):
    for i in range(n):
        catalan[n] = (catalan[n] + catalan[i] * catalan[n - 1 - i]) % MOD

for _ in range(T):
    L = int(input())
    
    # L이 홀수면 0 출력
    if L % 2 == 1:
        print(0)
    else:
        # L이 짝수면 카탈란 수 출력
        n = L // 2
        print(catalan[n])
