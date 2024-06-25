class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # ハッシュマップを初期化（要素の値をキー、そのインデックスを値として保存）
        index_map = {}
        # nums配列を走査し、各要素とそのインデックスを取得
        for i, num in enumerate(nums):
            # 要素がすでにハッシュマップに存在し、そのインデックス差がk以下かを確認
            if num in index_map and i - index_map[num] <= k:
                return True  # 条件を満たす場合、Trueを返す
            # 現在の要素とそのインデックスをハッシュマップに追加または更新
            index_map[num] = i
        # 最後まで条件を満たす要素が見つからなかった場合、Falseを返す
        return False
