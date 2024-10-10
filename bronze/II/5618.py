import sys
input = sys.stdin.readline

n = int(input()) # 2 or 3
nums = list(map(int, input().split()))

def get_divisors(num):
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return divisors

common_divisors = []

if len(nums) == 2:
    num1_divisors = get_divisors(nums[0])
    num2_divisors = get_divisors(nums[1])
    common_divisors = list(set(num1_divisors) & set(num2_divisors))
else:
    num1_divisors = get_divisors(nums[0])
    num2_divisors = get_divisors(nums[1])
    num3_divisors = get_divisors(nums[2])
    common_divisors = list(set(num1_divisors) & set(num2_divisors) & set(num3_divisors))

common_divisors.sort()
for divisor in common_divisors:
    print(divisor)
