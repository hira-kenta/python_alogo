def merge(data, start, mid, end):
    data_tmp = []
    i = start
    j = mid + 1

    while i <= mid and j <= end:
        if data[i] < data[j]:
            data_tmp.append(data[i])
            i += 1
        else:
            data_tmp.append(data[j])
            j += 1
        
    while i <= mid:
        data_tmp.append(data[i])
        i += 1

    while j <= end:
        data_tmp.append(data[j])
        j += 1
    
    k = start
    for val in data_tmp:
        data[k] = val
        k += 1

# data : マージソートするデータ 
# start: データの先頭
# end : データの末尾

def merge_sort(data, start, end):
    # ベースケース
    # 分割したデータが1つになった場合、再帰呼び出しを終了
    if start >= end:
        return

    # 中央となるデータ
    # 先頭データ + 末尾データ // 2
    mid = (start + end) // 2
    merge_sort(data, start, mid)   # 再帰処理(先頭データから中央値まで)
    merge_sort(data, mid + 1, end) # 再帰処理(中央値から末尾データまで)

    merge(data, start, mid, end)


data = [3, 8, 1, 2, -1, -10, 4]
end = len(data) - 1
merge_sort(data, 0, end)
print(data)