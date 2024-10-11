import sys
input = sys.stdin.readline

T = int(input())
Ns = list(map(int, input().split()))

def sum_multiples(n, k):
    count = n // k
    return k * count * (count + 1) // 2

for N in Ns:
    sum_three = sum_multiples(N, 3)
    sum_seven = sum_multiples(N, 7)
    sum_twenty_one = sum_multiples(N, 21)
    
    result = sum_three + sum_seven - sum_twenty_one
    print(result)
