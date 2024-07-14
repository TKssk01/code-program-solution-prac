from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # 配列が1つの要素しか持たない場合、到達可能なのでTrueを返す
        if len(nums) == 1:
            return True
        # 最初の要素が0の場合、次に進むことができないのでFalseを返す
        if nums[0] == 0:
            return False
        # 最初のインデックスの要素を最大到達可能範囲として設定する
        max_reach = nums[0]
        # 配列の2番目の要素から最後までループする
        for i in range(1, len(nums)):
            # 現在のインデックスが最大到達可能範囲を超えている場合、到達できないのでFalseを返す
            if i > max_reach:
                return False
            # 現在のインデックスからの最大到達可能範囲を更新する
            max_reach = max(max_reach, i + nums[i])
            # 最大到達可能範囲が配列の最後のインデックス以上になったらTrueを返す
            if max_reach >= len(nums) - 1:
                return True
        # 配列の最後までループしても終了条件に達しなかった場合、Falseを返す
        return False