# N, A, B = map(int, input().split())

# N = 100
# A = 4
# B = 16

# ans = 0

# for i in range(1, N + 1):
#     ones = i % 10
#     tens = (i % 100) // 10
#     hundreds = (i % 1000) // 100
#     thousands = (i % 10000) // 1000
#     tenthousands = (i % 100000) // 10000
#     sum = ones + tens + hundreds + thousands + tenthousands
#     if (A <= sum) and (sum <= B):
#         ans += i
# print(ans)

# ↑間違いではない
# 各桁の値を返してくれる関数に分離したい

def findSumOfDigit(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = n // 10
    return sum

N, A, B = map(int, input().split())

total = 0
for i in range(1, N + 1):
    sum = findSumOfDigit(i)
    if(sum >= A) and (sum <= B):
        total += i

print(total)