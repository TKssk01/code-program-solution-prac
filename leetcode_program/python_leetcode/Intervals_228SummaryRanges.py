from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:  # 配列が空の場合
            return []
        ranges = []  # 結果を格納するリスト
        start = nums[0]  # 現在の範囲の開始値
        for i in range(1, len(nums)):  # 配列の2番目の要素から最後までループ
            if nums[i] != nums[i - 1] + 1:  # 連続する数値でない場合
                if start == nums[i - 1]:  # 範囲が1つの数値のみの場合
                    ranges.append(f"{start}")  # 数値をそのまま追加
                else:
                    ranges.append(f"{start}->{nums[i - 1]}")  # 範囲を"開始->終了"の形式で追加
                start = nums[i]  # 新しい範囲の開始値を更新
        
        # 最後の範囲を処理
        if start == nums[-1]:  # 最後の数値が範囲の開始値と同じ場合
            ranges.append(f"{start}")  # 数値をそのまま追加
        else:
            ranges.append(f"{start}->{nums[-1]}")  # 範囲を"開始->終了"の形式で追加
        return ranges  # 結果のリストを返す
