from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        # グリッドの行数を取得
        m = len(grid)
        # グリッドの列数を取得
        n = len(grid[0])
        # DPテーブルを初期化、全ての値を0に設定
        dp = [[0] * n for _ in range(m)]
        # DPテーブルの左上をグリッドの左上の値で初期化
        dp[0][0] = grid[0][0]
        # 最初の行を埋める: 左から右に進む経路
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        # 最初の列を埋める: 上から下に進む経路
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        # DPテーブルを残りの部分を埋める
        for i in range(1, m):
            for j in range(1, n):
                # 左または上からの最小値に現在のセルの値を足す
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        # 右下の値を返す（最小コストの経路）
        return dp[m-1][n-1]
# テストケース
if __name__ == "__main__":
    solution = Solution()
    # テストケース 1: 例題のグリッド
    grid1 = [[1,3,1],[1,5,1],[4,2,1]]
    print(solution.minPathSum(grid1))  # 出力: 7
    # テストケース 2: 小さいグリッド
    grid2 = [[1,2,3],[4,5,6]]
    print(solution.minPathSum(grid2))  # 出力: 12
    # テストケース 3: 全てのセルが同じ値
    grid3 = [[1,1,1],[1,1,1],[1,1,1]]
    print(solution.minPathSum(grid3))  # 出力: 5
    # テストケース 4: 縦一列のグリッド
    grid4 = [[1],[2],[3]]
    print(solution.minPathSum(grid4))  # 出力: 6
    # テストケース 5: 横一列のグリッド
    grid5 = [[1,2,3]]
    print(solution.minPathSum(grid5))  # 出力: 6
    # テストケース 6: ランダムな大きなグリッド
    grid6 = [
        [1, 3, 1, 5],
        [2, 1, 4, 2],
        [5, 1, 1, 1],
        [4, 3, 2, 1]
    ]
    print(solution.minPathSum(grid6))  # 出力: 10