# マージソートサンプル①

def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2

    # 再帰的に分割
    left = merge_sort(data[0:mid]) # 左側を分割
    right = merge_sort(data[mid:]) # 右側を分割

    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:     # 左 <= 右のとき
            result.append(left[i])  # 左側から1つ取り出して追加
            i += 1
        else:
            result.append(right[j])  # 右側から1つ取り出して追加
            j += 1

    # 残りをまとめて追加
    if i < len(left):
        result.extend(left[i:])  # 左側の残りを追加
    if j < len(right):
        result.extend(right[j:]) # 右側の残りを追加
    
    return result

if __name__ == '__main__':
    data = [6, 15, 4, 2, 8, 5, 11, 9, 7, 13]
    sorted_data = merge_sort(data)
    print(f"{data} → {sorted_data}")
    
