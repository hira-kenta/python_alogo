# 入力
# N = int(input())
# H = list(map(int, input().split()))

N = 5
H = [8 ,6, 9, 2, 1]

# 動的計画法
dp = [ None ] *N  # 5個の空の配列を作る
dp[0] = 0         # 最初の要素に0を入れる=0番目の足場
for i in range(1, N):
    # 0番目の足場から1番目の足場にいくための消費体力
    if i == 1:
        dp[i] = abs(H[i - 1] - H[i])
    if i >= 2:
        v1 = dp[i - 1] + abs(H[i - 1] - H[i]) # 1個前の足場からジャンプするとき
        v2 = dp[i - 2] + abs(H[i - 2] - H[i]) # 2個前の足場からジャンプするとき
        dp[i] = min(v1, v2)

print(dp)
print(dp[N - 1])

