from typing import List
class Solution:
    def maxProfit(k: int, prices: list[int]) -> int:
        # 配列 prices の長さを取得
        n = len(prices)        
        # 株価リストが空の場合は利益を得ることができないので 0 を返す
        if n == 0:
            return 0
        # 取引回数 k が株価の長さの半分以上なら、無制限の取引とみなせる
        if k >= n // 2:
            # 無制限取引の場合、上昇するたびに売買することで利益を得る
            max_profit = 0
            # 1日目から順に価格差を計算して、利益を積み上げていく
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            # 最大利益を返す
            return max_profit
        # k 回の取引までで j 日目に得られる最大利益を記録する 2次元配列 dp を初期化
        dp = [[0] * n for _ in range(k + 1)]

        # i は取引回数 (1回目からk回目まで)
        for i in range(1, k + 1):
            # max_diff は過去の価格差と利益を基にして最適な購入日を決定するために使う
            max_diff = -prices[0]
            # j は日付 (1日目から最終日まで)
            for j in range(1, n):
                # 取引を行わない場合の最大利益と、売却して得られる利益の最大値を比較する
                dp[i][j] = max(dp[i][j - 1], prices[j] + max_diff)
                # max_diff を更新して、次の計算に備える
                max_diff = max(max_diff, dp[i - 1][j] - prices[j])
        # dp[k][-1] には k 回の取引で得られる最大利益が格納されている
        return dp[k][-1]
# テストケース
solution = Solution()
# 1回目のテスト: [2, 4, 1] において 2 回の取引で得られる最大利益は 2
print(solution.maxProfit(2, [2, 4, 1]))  # 出力: 2
# 2回目のテスト: [3, 2, 6, 5, 0, 3] において 2 回の取引で得られる最大利益は 7
print(solution.maxProfit(2, [3, 2, 6, 5, 0, 3]))  # 出力: 7
