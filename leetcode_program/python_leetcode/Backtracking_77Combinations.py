def combine(n, k):
    def backtrack(start, combination):
        # 現在の組み合わせの長さがkと等しい場合
        if len(combination) == k:
            # 結果リストに現在の組み合わせを追加
            result.append(combination[:])
            return
        # startからnまでの数字を順に見ていく
        for i in range(start, n + 1):
            # 現在の数字を組み合わせに追加
            combination.append(i)
            # 次の数字を追加するために再帰呼び出し
            backtrack(i + 1, combination)
            # 再帰呼び出しが終了したら、最後の数字を取り除いて元の状態に戻す
            combination.pop()
    # 結果を保持するリスト
    result = []
    # 再帰的に組み合わせを生成
    backtrack(1, [])
    # 全ての組み合わせを返す
    return result
# 例1
n = 4
k = 2
print(combine(n, k))  # [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]

# 例2
n = 1
k = 1
print(combine(n, k))  # [[1]]
