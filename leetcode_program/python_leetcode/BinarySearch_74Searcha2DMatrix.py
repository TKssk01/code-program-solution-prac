from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # 行列が空である場合は False を返す
        if not matrix or not matrix[0]:
            return False
        # 行数 (m) と列数 (n) を取得する
        m, n = len(matrix), len(matrix[0])
        # 二分探索の範囲を初期化する
        left, right = 0, m * n - 1
        # left が right 以下である限りループを続ける
        while left <= right:
            # mid を計算する
            mid = (left + right) // 2
            # mid を行列内の行と列に変換し、その値を取得する
            mid_value = matrix[mid // n][mid % n]
            # mid の値がターゲットと一致する場合
            if mid_value == target:
                return True
            # mid の値がターゲットより小さい場合
            elif mid_value < target:
                left = mid + 1
            # mid の値がターゲットより大きい場合
            else:
                right = mid - 1
        # ループが終了しても見つからなければ False を返す
        return False
