class Solution:
    def maximalSquare(matrix):
        # 行列が空の場合、0を返す
        if not matrix:
            return 0        
        # 行列の行数と列数を取得
        m, n = len(matrix), len(matrix[0])
        # dpテーブルを作成し、すべての値を0で初期化
        dp = [[0] * n for _ in range(m)]
        # 最大の正方形の一辺の長さを保持する変数
        max_side = 0
        # 行列を行ごとに走査
        for i in range(m):
            for j in range(n):
                # 現在のセルが '1' である場合
                if matrix[i][j] == '1':
                    # 最初の行または最初の列の場合、dp[i][j]は1になる
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        # 左上、上、左のセルの最小値に1を足す
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    
                    # 現在の最大の正方形の一辺の長さを更新
                    max_side = max(max_side, dp[i][j])
        
        # 最大の正方形の面積を計算して返す
        return max_side * max_side
# 例の入力
matrix1 = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
matrix2 = [["0","1"],["1","0"]]
matrix3 = [["0"]]
solution = Solution()
# 結果の出力
print(solution.maximalSquare(matrix1))  # 出力: 4
print(solution.maximalSquare(matrix2))  # 出力: 1
print(solution.maximalSquare(matrix3))  # 出力: 0
