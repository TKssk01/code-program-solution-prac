class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # word1とword2の長さを取得
        m, n = len(word1), len(word2)
        # DPテーブルの初期化（サイズは(m+1) x (n+1)）
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        # word1が空の場合の初期条件（word2を作るためにj回の挿入が必要）
        for i in range(1, m + 1):
            dp[i][0] = i
        # word2が空の場合の初期条件（word1を削除するためにi回の削除が必要）
        for j in range(1, n + 1):
            dp[0][j] = j
        # DPテーブルを更新していく
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # もし現在の文字が一致するなら、置換は不要
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 文字が一致しない場合、挿入、削除、置換のうち最小の操作を選択
                    dp[i][j] = min(dp[i-1][j-1] + 1,  # 置換
                                   dp[i][j-1] + 1,    # 挿入
                                   dp[i-1][j] + 1)    # 削除
        # DPテーブルの最終的な値が最小操作回数
        return dp[m][n]
# テストケース
solution = Solution()
# テストケース1: "horse" -> "ros"
word1 = "horse"
word2 = "ros"
print(f"Test Case 1: {solution.minDistance(word1, word2)}")  # Expected output: 3
# テストケース2: "intention" -> "execution"
word1 = "intention"
word2 = "execution"
print(f"Test Case 2: {solution.minDistance(word1, word2)}")  # Expected output: 5