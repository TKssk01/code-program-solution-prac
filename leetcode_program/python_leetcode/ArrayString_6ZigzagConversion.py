class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # 1. 特殊ケースの処理
        if numRows == 1 or numRows >= len(s):
            return s
        # 2. 行を格納するリストの作成
        rows = [''] * numRows  # 例えば、numRows = 3 の場合、['', '', ''] となる
        current_row = 0  # 現在の行を追跡するための変数
        direction = -1  # 移動方向を管理する変数、最初はどちらでも良い
        # 3. 文字列のジグザグ配置
        for char in s:
            rows[current_row] += char  # 現在の行に文字を追加する
            # 方向を変えるかどうかを判断する
            if current_row == 0 or current_row == numRows - 1:
                direction *= -1  # 方向を反転させる
            current_row += direction  # 行を進める
        # 4. 最終的な文字列の生成
        return ''.join(rows)  # 各行を連結して最終的な文字列を作る