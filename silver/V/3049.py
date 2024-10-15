import sys
input = sys.stdin.readline

N = int(input())

# nC4
print(N*(N-1)*(N-2)*(N-3)//24)
