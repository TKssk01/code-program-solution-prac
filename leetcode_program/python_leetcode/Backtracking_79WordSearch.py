# 必要なライブラリのインポート
from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # DFSによる探索を行う関数を定義
        def dfs(i, j, k):
            # wordのすべての文字が見つかった場合、Trueを返す
            if k == len(word):
                return True
            # グリッドの範囲外、または文字が一致しない場合、Falseを返す
            if (i < 0 or i >= len(board) or 
                j < 0 or j >= len(board[0]) or 
                board[i][j] != word[k]):
                return False
            # 現在のセルの文字を一時的に保存
            temp = board[i][j]
            # 現在のセルを訪問済みとしてマーク
            board[i][j] = '#'  # マークして再訪問を防ぐ
            # 上下左右の4方向に探索を進める
            result = (dfs(i+1, j, k+1) or  # 下
                      dfs(i-1, j, k+1) or  # 上
                      dfs(i, j+1, k+1) or  # 右
                      dfs(i, j-1, k+1))    # 左
            # 探索が終わったら、セルを元の状態に戻す
            board[i][j] = temp  # 元に戻す
            # 探索結果を返す
            return result
        # グリッドの各セルを開始点として探索
        for i in range(len(board)):
            for j in range(len(board[0])):
                # 現在のセルから探索を開始し、成功したらTrueを返す
                if dfs(i, j, 0):
                    return True
        # すべての開始点を試してもwordが見つからなかった場合、Falseを返す
        return False