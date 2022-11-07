# 入力
N = int(input())
field = [input() for _ in range(N)]

# DP 配列の定義(配列全体を0で初期化)
dp = [[0] * N for _ in range(N)]

# 初期値(左上のマスはすでに到達しているので1通り)
dp[0][0] = 1

# マスを順に埋めていく
for i in range(N):
  for j in range(N):
    #　穴マスである場合はスキップ
    if field[i][j] == '#':
      continue
    
    # 上からくる場合
    if i - 1 >= 0:
      dp[i][j] += dp[i - 1][j]

    # 左からくる場合
    if j - 1 >= 0:
      dp[i][j] += dp[i][j - 1]

print(dp[N - 1][N - 1])