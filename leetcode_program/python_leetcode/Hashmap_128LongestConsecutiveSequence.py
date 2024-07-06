from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0  # 配列が空の場合は0を返す
        num_set = set(nums)  # 配列の要素をセットに変換して重複を取り除く
        longest_streak = 0  # 最長の連続シーケンスの長さを記録する変数
        for num in num_set:
            # シーケンスの開始要素を特定
            if num - 1 not in num_set:  # num - 1 がセットに存在しない場合、numは新しいシーケンスの開始要素
                current_num = num
                current_streak = 1  # 現在のシーケンスの長さを1に設定
                # 連続する要素を追跡
                while current_num + 1 in num_set:  # current_num + 1 がセットに存在する限りループ
                    current_num += 1
                    current_streak += 1  # シーケンスの長さを増加
            # 最長シーケンスの長さを更新
                longest_streak = max(longest_streak, current_streak)
        return longest_streak  # 最終的な最長シーケンスの長さを返す