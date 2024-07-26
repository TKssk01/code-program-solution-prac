# キューを使用するためにdequeをインポート
from collections import deque
from typing import List

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # ボードのサイズを取得
        n = len(board)
        # 目標となるマスの番号を設定
        target = n * n
        def get_coordinates(num):
            # マス番号から行番号を計算（0-indexed）
            row = (num - 1) // n
            # マス番号から列番号を計算（0-indexed）
            col = (num - 1) % n
            # 奇数行の場合、列番号を反転（Boustrophedon style）
            if row % 2 == 1:
                col = n - 1 - col
            # ボードの下から数えた行番号と列番号を返す
            return n - 1 - row, col
        # BFSのためのキューを初期化（開始位置と移動回数）
        queue = deque([(1, 0)])  # (current position, moves)
        # 訪れたマスを記録するセット
        visited = set()
        # キューが空になるまでBFSを続ける
        while queue:
            # キューから現在の位置と移動回数を取り出す
            pos, moves = queue.popleft()
            # 現在の位置から1~6マス先までの全ての可能な移動先をチェック
            for next_pos in range(pos + 1, min(pos + 7, target + 1)):
                # 次の位置の座標を取得
                r, c = get_coordinates(next_pos)
                # その位置に蛇や梯子がある場合、移動先を更新
                if board[r][c] != -1:
                    next_pos = board[r][c]
                # 目標に到達した場合、移動回数を返す
                if next_pos == target:
                    return moves + 1
                # 新しい位置をまだ訪れていない場合
                if next_pos not in visited:
                    # 訪れたマスとしてマーク
                    visited.add(next_pos)
                    # キューに新しい位置と更新された移動回数を追加
                    queue.append((next_pos, moves + 1))
        # 目標に到達できなかった場合は-1を返す
        return -1