import sys
input = sys.stdin.readline

N = int(input())
MOD = 1000000000

# 완전 순열
def derangement(n):
    dp = [0] * (n + 1)
    dp[1] = 0
    dp[2] = 1
    for i in range(3, n + 1):
        dp[i] = (i - 1) * (dp[i - 1] + dp[i - 2]) % MOD
    return dp[n]

print(derangement(N))
