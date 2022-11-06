N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# 動的計画法の配列を用意する
dp = [[0] * 3 for _ in range(N)]

# 0日目の情報をセットする
for i in range(3):
    dp[0][i] = A[0][i]

# 1, 2...日目の報酬を求める
for i in range(1, N):
    dp[i][0] = max(dp[i-1][1], dp[i-1][2]) + A[i][0]
    dp[i][1] = max(dp[i-1][0], dp[i-1][2]) + A[i][1]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1]) + A[i][2]

# dp[N - 1][0], dp[N - 1][1], dp[N - 1][2]の最大値を出力
print(max(dp[N - 1]))