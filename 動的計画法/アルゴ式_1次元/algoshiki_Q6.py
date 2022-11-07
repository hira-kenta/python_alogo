# n , m = map(int,input().split())
# d = list(map(int, input().split()))

n,m = 7, 4
d = [2, 3, 5, 6]

# 動的計画法の舞台となる配列
dp = [False] * (n + 1)

# マス0には初めから到達している
dp[0] = True

# 順に計算していく
for i in range(1, n + 1):
    for j in range(0, m):
        if i - d[j] >= 0 and dp[i - d[j]]:
            dp[i] = True

print("Yes" if dp[n] else "No")
