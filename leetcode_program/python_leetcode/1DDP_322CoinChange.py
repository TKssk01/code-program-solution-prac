from typing import List
# ソリューションクラスの定義
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp配列を作成し、全ての要素を amount + 1 に初期化する
        # (amount + 1 は「非常に大きな値」として設定し、初期化として使用する)
        dp = [amount +  1] * (amount + 1)
        # 金額0を作るために必要な硬貨の枚数は0
        dp[0] = 0
        # 各硬貨の額面についてループを回す
        for coin in coins:
            # 金額coinからamountまでループを回し、各金額での最小硬貨枚数を計算する
            for i in range(coin, amount + 1):
                # 現在のdp[i]の値と、dp[i - coin] + 1の値を比較し、小さい方をdp[i]に設定
                # これは、硬貨coinを使った場合と使わなかった場合のどちらが少ない硬貨枚数かを決定する
                dp[i] = min(dp[i], dp[i - coin] + 1)
        # 金額amountを作るために必要な最小の硬貨枚数を返す
        # もし、dp[amount]が初期値のままなら、金額を作ることができないので-1を返す
        return dp[amount] if dp[amount] != amount + 1 else -1
# ソリューションのインスタンスを作成
solution = Solution()
# テストケース1
coins = [1, 2, 5]
amount = 11
print(solution.coinChange(coins, amount))  # 出力: 3 (11 = 5 + 5 + 1)
# テストケース2
coins = [2]
amount = 3
print(solution.coinChange(coins, amount))  # 出力: -1 (3を作ることはできない)
# テストケース3
coins = [1]
amount = 0
print(solution.coinChange(coins, amount))  # 出力: 0 (0円を作るために硬貨は不要)
# テストケース4
coins = [1, 2, 5]
amount = 100
print(solution.coinChange(coins, amount))  # 出力: 20 (100 = 5 * 20)
# テストケース5
coins = [2, 5, 10, 1]
amount = 27
print(solution.coinChange(coins, amount))  # 出力: 4 (27 = 10 + 10 + 5 + 2)