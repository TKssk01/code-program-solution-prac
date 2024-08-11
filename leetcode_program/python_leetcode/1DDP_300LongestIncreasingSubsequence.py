from typing import List
import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 厳密に増加する部分列の末尾の値を保持するリストを初期化
        tails = []
        # nums 配列の各要素に対して処理を行う
        for num in nums:
            # tails の中で num が挿入できる位置を二分探索で探す
            pos = bisect.bisect_left(tails, num)
            # pos が tails の末尾であれば、num を追加
            if pos == len(tails):
                tails.append(num)
            # そうでなければ、tails[pos] を num で置き換える
            else:
                tails[pos] = num
        # tails の長さが最長の厳密に増加する部分列の長さとなる
        return len(tails)
