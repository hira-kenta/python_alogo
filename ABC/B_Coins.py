# A = int(input())
# B = int(input())
# C = int(input())
# X = int(input())

A = 30
B = 40
C = 50
X = 6000

res = 0

for i in range(0, A + 1):
    for j in range(0, B + 1):
        for k in range(0, C + 1):
            sum = (i * 500) + (j * 100) + (k * 50)
            if sum == X:
                res += 1

print(res)