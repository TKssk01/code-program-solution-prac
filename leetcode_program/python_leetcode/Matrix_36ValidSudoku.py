from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 各行が有効かチェック
        for row in board:
            if not self.isValidUnit(row):
                return False  # 無効な行があればFalseを返す
        # 各列が有効かチェック
        for col in zip(*board):
            if not self.isValidUnit(col):
                return False  # 無効な列があればFalseを返す
        # 各3x3のサブボックスが有効かチェック
        for i in range(0, 9, 3):  # 3行ごとにサブボックスをチェック
            for j in range(0, 9, 3):  # 3列ごとにサブボックスをチェック
                if not self.isValidSubBox(board, i, j):
                    return False  # 無効なサブボックスがあればFalseを返す
        return True  # 全ての行、列、サブボックスが有効ならTrueを返す
    def isValidUnit(self, unit: List[str]) -> bool:
        # 空のセル（‘.’）を取り除く
        unit = [x for x in unit if x != '.']
        # 重複がないかチェック（セットのサイズとリストのサイズが同じであることを確認）
        return len(unit) == len(set(unit))
    def isValidSubBox(self, board: List[List[str]], start_row: int, start_col: int) -> bool:
        # 3x3のサブボックスの要素を収集
        sub_box = []
        for i in range(3):  # サブボックス内の各行をチェック
            for j in range(3):  # サブボックス内の各列をチェック
                cell = board[start_row + i][start_col + j]  # 現在のセルを取得
                if cell != '.':
                    sub_box.append(cell)  # 空でなければサブボックスに追加
        # サブボックスが有効かチェック
        return self.isValidUnit(sub_box)