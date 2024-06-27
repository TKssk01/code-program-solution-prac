from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 左側のポインターを初期化
        left = 0
        # 右側のポインターを初期化
        right = len(height) - 1
        # 最大面積を保存する変数を初期化
        max_area = 0
        # 左ポインターが右ポインターを越えない限りループを続ける
        while left < right:
            # 現在の幅を計算
            width = right - left
            # 現在の面積を計算（低い方の高さ×幅）
            current_area = min(height[left], height[right]) * width
            # 最大面積を更新
            max_area = max(max_area, current_area)
            # 低い方のポインターを動かす（高さが低い方を動かすことで、次に大きい面積を狙う）
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # 最大面積を返す
        return max_area