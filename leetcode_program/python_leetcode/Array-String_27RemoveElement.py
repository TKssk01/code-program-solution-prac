from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # ループを開始。'nums'リストに'val'が含まれている間はループを続ける。
        while val in nums:
            # 'nums'リストから最初に見つかる'val'の値を削除する。
            nums.remove(val)
        # ループが終了したら、'nums'リストの長さを返す。
        return nums
    
