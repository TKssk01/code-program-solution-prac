from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # トライアングルの行数を取得
        n = len(triangle)
        # 最下層から2番目の行から上に向かって順に処理
        for row in range(n - 2, -1, -1):
            # 現在の行の各要素に対して処理を行う
            for col in range(len(triangle[row])):
                # 次の行の隣接する2つの値のうち小さい方を選び、それを現在の値に加算
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        # 最上部の値が最小経路和となるため、それを返す
        return triangle[0][0]
