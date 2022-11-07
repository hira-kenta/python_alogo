# 入力
N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]

# DP配列の定義(配列全体を0で初期化)
dp = [[0] * N for _ in range(N)]

# 初期値(左上のマスをセット)
dp[0][0] = field[0][0]

# マスを順に埋めていく
for i in range(N):
  for j in range(N):
    # 上からくる場合
    if i - 1 >= 0:
      dp[i][j] = max(dp[i][j], dp[i - 1][j] + field[i][j])

    # 左からくる場合
    if j - 1 >= 0:
      dp[i][j] = max(dp[i][j], dp[i][j - 1] + field[i][j])

print(dp[N - 1][N - 1])