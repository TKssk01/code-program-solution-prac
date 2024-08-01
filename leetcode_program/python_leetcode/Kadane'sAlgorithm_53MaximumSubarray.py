from typing import List  # List 型をインポート

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # 初期化：最初の要素を max_sum と current_sum に設定
        max_sum = nums[0]
        current_sum = nums[0]
        # 配列の2番目の要素から最後の要素までをループ
        for i in range(1, len(nums)):
            # current_sum を更新：現在の要素と、現在の要素を含む current_sum の大きい方を選択
            current_sum = max(nums[i], current_sum + nums[i])
            # max_sum を更新：現在の max_sum と current_sum の大きい方を選択
            max_sum = max(max_sum, current_sum)
        # 最大部分配列の和を返す
        return max_sum
