import heapq

def kSmallestPairs(nums1, nums2, k):
    # nums1, nums2のいずれかが空、またはkが0の場合は空リストを返す
    if not nums1 or not nums2 or k == 0:
        return []
    # 最小ヒープを初期化
    min_heap = []
    # nums1の各要素とnums2の最初の要素のペアを作成し、ヒープに格納
    for i in range(min(k, len(nums1))):
        # (ペアの和, nums1のインデックス, nums2のインデックス)をヒープにプッシュ
        heapq.heappush(min_heap, (nums1[i] + nums2[0], i, 0))
    # 結果を格納するリスト
    result = []
    # ヒープが空でなく、結果の長さがk未満の間ループを続ける
    while min_heap and len(result) < k:
        # 最小のペアをヒープから取り出す
        sum_val, i, j = heapq.heappop(min_heap)
        # 取り出したペアを結果リストに追加
        result.append([nums1[i], nums2[j]])
        # 次の候補ペアをヒープに追加（同じnums1の要素とnums2の次の要素のペア）
        if j + 1 < len(nums2):
            heapq.heappush(min_heap, (nums1[i] + nums2[j + 1], i, j + 1))
    # 結果のリストを返す
    return result

# テストケース
print(kSmallestPairs([1, 7, 11], [2, 4, 6], 3))  # [[1,2],[1,4],[1,6]]
print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))  # [[1,1],[1,1]]
