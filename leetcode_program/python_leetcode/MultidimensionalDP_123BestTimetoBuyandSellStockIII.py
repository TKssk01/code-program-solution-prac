from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 空のリストが与えられた場合、利益は0
        if not prices:
            return 0
        # pricesの長さを取得
        n = len(prices)
        # 左側の取引の最大利益を格納するリストを初期化
        left_profits = [0] * n
        # 右側の取引の最大利益を格納するリストを初期化
        right_profits = [0] * n
        # 最小の価格を最初の値で初期化
        min_price = prices[0]
        # 前方から最大利益を計算
        for i in range(1, n):
            # 現在までの最小価格を更新
            min_price = min(min_price, prices[i])
            # i日目までの最大利益を更新
            left_profits[i] = max(left_profits[i - 1], prices[i] - min_price)
        # 最大の価格を最後の値で初期化
        max_price = prices[-1]
        # 後方から最大利益を計算
        for i in range(n - 2, -1, -1):
            # 現在までの最大価格を更新
            max_price = max(max_price, prices[i])
            # i日目以降の最大利益を更新
            right_profits[i] = max(right_profits[i + 1], max_price - prices[i])
        # 2回の取引で得られる最大利益を計算
        max_profit = 0
        for i in range(n):
            # 左側の取引と右側の取引の利益の合計を最大化
            max_profit = max(max_profit, left_profits[i] + right_profits[i])
        # 最終的な最大利益を返す
        return max_profit