from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # 結果を格納するためのリストを初期化
        merged = []
        i = 0
        n = len(intervals)

        # 新しい区間の前にある既存の区間を結果リストに追加
        while i < n and intervals[i][1] < newInterval[0]:
            merged.append(intervals[i])
            i += 1

        # 新しい区間と重なる既存の区間を結合
        while i < n and intervals[i][0] <= newInterval[1]:
            # 重なる区間の開始位置を決定（最小値を取る）
            newInterval[0] = min(newInterval[0], intervals[i][0])
            # 重なる区間の終了位置を決定（最大値を取る）
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        
        # 重なった結果の新しい区間を結果リストに追加
        merged.append(newInterval)

        # 新しい区間の後にある既存の区間を結果リストに追加
        while i < n:
            merged.append(intervals[i])
            i += 1
        
        # 結果リストを返す
        return merged
