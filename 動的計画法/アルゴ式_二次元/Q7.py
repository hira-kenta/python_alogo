N = int(input())
A = [list(map(int,input().split())) for _ in range(N)]

# DP 配列の定義(配列全体をINFで初期化)
INF = 1000000
dp = [[INF] * N for _ in range(N)]

# 初期値(右上のマスの値をセット)
dp[0][N - 1] = A[0][N - 1]

# マスを順に埋めていく
for i in range(N):
  for j in reversed(range(N)):
    # 上からくる場合
    if i - 1 >= 0:
      dp[i][j] = min(dp[i][j], dp[i-1][j] + A[i][j])

    # 右からくる場合
    if j + 1 < N:
      dp[i][j] = min(dp[i][j], dp[i][j + 1] + A[i][j])


# 出力
print(dp[N - 1][0])