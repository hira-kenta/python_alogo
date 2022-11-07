# N = int(input())
# A = list(map(int, input().split()))

N = 3
A = [8, 12, 40]

cnt = 0  #　何回操作できるか

while True:
    exist_odd = False
    for i in range(0, N):
        if A[i] % 2 != 0:  #奇数である場合
            exist_odd = True
    
    if exist_odd:
        break
    
    for i in range(0, N):
        A[i] = A[i] // 2
    cnt += 1

print(cnt)