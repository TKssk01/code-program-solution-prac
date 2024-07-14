from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 子供の数を取得
        n = len(ratings)
        # 全ての子供に最初に1つずつキャンディーを配る
        candies = [1] * n
        # 左から右へのパス
        for i in range(1, n):
            # 現在の子供の評価が左隣の子供より高い場合
            if ratings[i] > ratings[i-1]:
                # 左隣の子供のキャンディー数 + 1 を配る
                candies[i] = candies[i-1] + 1
        # 右から左へのパス
        for i in range(n-2, -1, -1):
            # 現在の子供の評価が右隣の子供より高い場合
            if ratings[i] > ratings[i+1]:
                # 右隣の子供のキャンディー数 + 1 と現在の数の大きい方を選択
                candies[i] = max(candies[i], candies[i+1] + 1)
        # 全てのキャンディー数の合計を返す
        return sum(candies)