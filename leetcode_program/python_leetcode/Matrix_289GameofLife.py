from typing import List

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        board を直接変更し、次の状態を生成する
        """
        # ボードの行数と列数を取得
        m, n = len(board), len(board[0])
        def count_live_neighbors(i, j):
            """隣接する生きているセルの数を数える関数"""
            count = 0
            # 周囲8方向をチェック
            for di in [-1, 0, 1]:
                for dj in [-1, 0, 1]:
                    # 自分自身はスキップ
                    if di == 0 and dj == 0:
                        continue
                    # 隣接セルの座標を計算
                    ni, nj = i + di, j + dj
                    # ボードの範囲内かつ生きているセル（1）または生きていたが死ぬセル（3）の場合カウント
                    if 0 <= ni < m and 0 <= nj < n and board[ni][nj] in [1, 3]:
                        count += 1
            return count
        # ボードの全セルを走査
        for i in range(m):
            for j in range(n):
                # 隣接する生きているセルの数を取得
                live_neighbors = count_live_neighbors(i, j)
                
                if board[i][j] == 1:  # 現在生きているセルの場合
                    if live_neighbors < 2 or live_neighbors > 3:
                        # 過疎または過密で死ぬ場合、3にマーク（後で0に変更）
                        board[i][j] = 3
                else:  # 現在死んでいるセルの場合
                    if live_neighbors == 3:
                        # 周囲に3つの生きたセルがある場合、2にマーク（後で1に変更）
                        board[i][j] = 2
        # 最終的な状態に更新
        for i in range(m):
            for j in range(n):
                if board[i][j] == 2:
                    # 2は死んでいたセルが生き返るケース
                    board[i][j] = 1
                elif board[i][j] == 3:
                    # 3は生きていたセルが死ぬケース
                    board[i][j] = 0