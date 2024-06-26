from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 数値とインデックスをマッピングする辞書
        num_to_index = {}
        # 配列を一度だけ走査する
        for index, num in enumerate(nums):
            # 目標値と現在の数値の差を計算
            complement = target - num
            # もし差の値が既に辞書にあれば、ペアが見つかったことになる
            if complement in num_to_index:
                return [num_to_index[complement], index]
            # 辞書に現在の数値とそのインデックスを保存
            num_to_index[num] = index
        # 解が見つからない場合は空のリストを返す
        return []