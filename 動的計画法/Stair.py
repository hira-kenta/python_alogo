N = int(input())

# 動的計画法
dp = [None] * N + 1
for i in range(N + 1):
    if i <= 1:
        dp[i] = 1
    else:
        dp[i] = dp[i - 1] + dp[i - 2]

print(dp[N])
# フィボナッチ数列と同じ漸化式になる