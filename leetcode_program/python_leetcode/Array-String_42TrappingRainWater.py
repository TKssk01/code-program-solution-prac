from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        # 高さの配列が空であれば、溜まる水はない
        if not height:
            return 0
        n = len(height)  # 高さの配列の長さを取得
        left_max = [0] * n  # 左側からの最大値を保持する配列を初期化
        right_max = [0] * n  # 右側からの最大値を保持する配列を初期化
        # 左側からの最大値を計算
        left_max[0] = height[0]  # 最初の要素の左側からの最大値を初期化
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], height[i])  # 現在位置の左側最大値を更新
        # 右側からの最大値を計算
        right_max[n - 1] = height[n - 1]  # 最後の要素の右側からの最大値を初期化
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], height[i])  # 現在位置の右側最大値を更新
        water_trapped = 0  # 溜まる水の量を初期化
        # 各位置での溜まる水の量を計算
        for i in range(n):
            # 左右の最大値の小さい方と現在の高さとの差分を計算し、0未満の場合は0とする
            water_trapped += max(0, min(left_max[i], right_max[i]) - height[i])
        return water_trapped  # 総合的に溜まる水の量を返す
# 例1
height1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(Solution().trap(height1))  # 出力: 6
# 例2
height2 = [4, 2, 0, 3, 2, 5]
print(Solution().trap(height2))  # 出力: 9
