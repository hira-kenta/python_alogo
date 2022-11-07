# 無限大を表す数値過
INF = 10000000

# 入力
# n, m = map(int(input()))
# a = list(map(int, input().split()))
n, m = 8, 4
a = [3, 1 ,4, 1, 5, 9, 2, 6]

# 計算の舞台となる配列を宣言
dp = [INF] * n

# 初期値
dp[0] = 0

# 順に計算していく
for i in range(1, n):
    for j in range(1, m + 1):
        if i - j >= 0:
            dp[i] = min(dp[i], dp[i - j] + a[i] * j)
print(dp[n - 1])
