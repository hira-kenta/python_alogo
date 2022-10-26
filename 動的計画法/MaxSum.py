N = int(input())
A = list(map(int, input().split()))

# N＋1個の配列を作成
# N:3の場合、dp[0]～dp[3]
dp = [None] * (N + 1)

# 初期値を設定
dp[0] = 0
for i in range(0, N):
    # 次項の数との和と、足さない数とどちらか大きい方を入れる
    dp[i + 1] = max(dp[i], dp[i] + A[i])

print(dp[N])