from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []  # 結果を格納するリスト
        if not matrix:
            return result  # 行列が空の場合は空のリストを返す
        # 境界を初期化
        top, bottom = 0, len(matrix) - 1  # 上と下の境界
        left, right = 0, len(matrix[0]) - 1  # 左と右の境界
        # 境界が交差しない限りループを続ける
        while top <= bottom and left <= right:
            # 上の行を左から右へ走査
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1  # 上の境界を1行下げる
            # 右の列を上から下へ走査
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1  # 右の境界を1列左へ移動する
            # 下の行を右から左へ走査（もしtopがbottomを越えていなければ）
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1  # 下の境界を1行上げる
            # 左の列を下から上へ走査（もしleftがrightを越えていなければ）
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1  # 左の境界を1列右へ移動する
        return result  # 螺旋順に取り出した要素のリストを返す
# テストケース
matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print(Solution().spiralOrder(matrix1))  # 出力: [1, 2, 3, 6, 9, 8, 7, 4, 5]
print(Solution().spiralOrder(matrix2))  # 出力: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
