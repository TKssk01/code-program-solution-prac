# リスト型を使用するためのインポート
from typing import List
# ソリューションクラスの定義
class Solution:
    # findMinメソッドの定義、numsというリストを引数に取る
    def findMin(self, nums: List[int]) -> int:
        # 初期化: 左端(left)と右端(right)のインデックスを設定
        left, right = 0, len(nums) - 1
        # 左端が右端より小さい間ループを続ける
        while left < right:
            # 中央インデックスを計算
            mid = (left + right) // 2
            # nums[mid] が nums[right] より大きい場合、最小値は右半分にある
            if nums[mid] > nums[right]:
                # 左端をmid + 1に更新
                left = mid + 1
            else:
                # nums[mid] が nums[right] より小さいか等しい場合、最小値は左半分にある
                # 右端をmidに更新
                right = mid
        # ループ終了後、leftが最小値のインデックスを指す
        return nums[left]
