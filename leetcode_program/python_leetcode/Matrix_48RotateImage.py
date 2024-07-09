from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 行列のサイズを取得
        n = len(matrix)
        # 行列の転置を行う
        for i in range(n):
            for j in range(i, n):
                # i行j列の要素とj行i列の要素を交換する
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 各行を逆順に並べ替える
        for i in range(n):
            # i番目の行を反転する
            matrix[i].reverse()
