from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        ボード上の囲まれた領域を捕獲する（'O'を'X'に変更する）
        board: 'X'と'O'で構成される2次元リスト
        戻り値: None（ボードを直接変更する）
        """
        # ボードが空または無効な場合、処理を終了
        if not board or not board[0]:
            return
        
        # ボードの行数(m)と列数(n)を取得
        m, n = len(board), len(board[0])

        def dfs(i: int, j: int) -> None:
            """
            深さ優先探索（DFS）で連続した'O'をマークする内部関数
            i, j: 現在の座標
            """
            # 以下の場合、探索を終了:
            # 1. ボードの範囲外
            # 2. 現在のセルが'O'でない（既に探索済みか、'X'である）
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != 'O':
                return
            
            # 現在のセルを'T'（Temporary）でマーク
            # 'T'は境界に接続された'O'を示す一時的なマーカー
            board[i][j] = 'T'
            
            # 隣接する4方向（上下左右）のセルに対してDFSを再帰的に呼び出し
            dfs(i+1, j)  # 下
            dfs(i-1, j)  # 上
            dfs(i, j+1)  # 右
            dfs(i, j-1)  # 左

        # ステップ1: ボードの境界にある'O'とそれに接続された'O'をマーク
        # 左右の列をチェック
        for i in range(m):
            dfs(i, 0)      # 左端の列
            dfs(i, n-1)    # 右端の列
        
        # 上下の行をチェック（角は既にチェック済みなので除外可能）
        for j in range(1, n-1):
            dfs(0, j)      # 上端の行
            dfs(m-1, j)    # 下端の行

        # ステップ2: ボード全体を走査し、'O'と'T'を適切に処理
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    # 'O'のままのセルは囲まれた領域なので'X'に変更（捕獲）
                    board[i][j] = 'X'
                elif board[i][j] == 'T':
                    # 'T'でマークされたセルは境界に接続されているので'O'に戻す
                    board[i][j] = 'O'

        # この時点で、ボードは以下のように更新されている：
        # - 元々の'X'はそのまま'X'
        # - 境界に接続されていた'O'は一度'T'になり、その後'O'に戻された
        # - 囲まれていた'O'は'X'に変更された
        