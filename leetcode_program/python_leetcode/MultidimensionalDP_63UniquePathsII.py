from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # グリッドの行数mと列数nを取得
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        # DPテーブルを初期化（すべてのセルを0で初期化）
        dp = [[0] * n for _ in range(m)]
        # ロボットが最初にいる位置に到達可能かを設定
        dp[0][0] = 1 if obstacleGrid[0][0] == 0 else 0
        # 最初の行を処理：障害物がない限り右に進む
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        # 最初の列を処理：障害物がない限り下に進む
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        # DPテーブルを更新：上のセルと左のセルから経路数を加算
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    # 障害物がない場合、上からの経路数と左からの経路数を足す
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                else:
                    # 障害物がある場合、そのセルは通れないので経路数は0
                    dp[i][j] = 0
        # 最終的なユニークな経路数を返す
        return dp[-1][-1]
