from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 行数と列数を取得
        rows, cols = len(matrix), len(matrix[0])
        # 最初の行に0があるかどうかのフラグ
        row_zero = False
        # 最初の列に0があるかどうかのフラグ
        col_zero = False
        # 行列を走査して0がある行と列を記録する
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # 最初の行に0がある場合
                    if i == 0: row_zero = True
                    # 最初の列に0がある場合
                    if j == 0: col_zero = True
                    # 0の情報を最初の行と列に記録する
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        # 記録に基づいて行と列を0に設定する（最初の行と列を除く）
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        # 必要に応じて最初の行を0に設定
        if row_zero:
            for j in range(cols):
                matrix[0][j] = 0
        # 必要に応じて最初の列を0に設定
        if col_zero:
            for i in range(rows):
                matrix[i][0] = 0