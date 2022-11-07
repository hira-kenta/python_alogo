# N = int(input())
# A = list(map(int, input().split()))

# N = 3
# A = [10, 20, 30]

# dp = [[None] * N for i in range(N)]

# for i in range(N):
#     dp[0][i] = A[i]

# for i in range(1, N):
#     for j in range(0, N):
#         sum = 0
#         sum += dp[i - 1][j]
        
#         if j == 0:
#             sum += dp[i - 1][j + 1]
#         elif j == (N - 1):
#             sum += dp[i - 1][j - 1]
#         else:
#             sum += dp[i - 1][j - 1] + dp[i - 1][j + 1]
        
#         dp[i][j] = sum % 100

# print(dp[N - 1][N - 1])


# 解答例(↑のが速かった)
# 関数を用意するのもあり
# a に b を足して100で割った余りを返す関数
def add(a, b):
    a += b
    return a % 100

N = int(input())

# N * N　の配列を用意する
A = [[0]* N for _ in range(N)]

# 0行目の入力を受け取る
A[0] = list(map(int, input().split()))

for i in range(1, N):
    for j in range(N):
        # 真上を足す
        A[i][j] = add(A[i][j], A[i-1][j])

        # 左上を足す
        if j - 1 >= 0:
            A[i][j] = add(A[i][j], A[i - 1][j - 1])

        # 右上を足す
        if j + 1 < N:
            A[i][j] = add(A[i][j], A[i - 1][j + 1])

print(A[N - 1][N - 1])