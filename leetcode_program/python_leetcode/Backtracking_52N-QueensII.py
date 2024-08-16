def totalNQueens(n: int) -> int:
    # 結果を格納する変数。解の数を数えるために使用する。
    solutions = 0
    # クイーンの配置をチェックするためのセット
    # columns: 既にクイーンが置かれている列を記録
    # diagonal1: 左上から右下への対角線 (row - col) を記録
    # diagonal2: 右上から左下への対角線 (row + col) を記録
    columns = set()
    diagonal1 = set()  # 左上から右下への対角線 (row - col)
    diagonal2 = set()  # 右上から左下への対角線 (row + col)
    # バックトラッキングを行うための関数
    def backtrack(row):
        nonlocal solutions  # 外部のsolutions変数を使用することを宣言
        # もし全ての行にクイーンを配置できた場合
        if row == n:
            # 解を見つけたので、解の数を1つ増やす
            solutions += 1
            return
        # 現在の行にクイーンを配置するために、全ての列を試す
        for col in range(n):
            # クイーンが置けるかチェック
            # すでに同じ列、同じ対角線にクイーンがあるか確認
            if col in columns or (row - col) in diagonal1 or (row + col) in diagonal2:
                continue  # この列には置けないので次の列へ
            # 現在の列と対角線を使用済みとしてマークする
            columns.add(col)
            diagonal1.add(row - col)
            diagonal2.add(row + col)
            # 次の行にクイーンを配置することを試みる
            backtrack(row + 1)
            # バックトラッキングのために、配置したクイーンを取り除く
            columns.remove(col)
            diagonal1.remove(row - col)
            diagonal2.remove(row + col)
    # 最初の行からスタート
    backtrack(0)
    # 全ての解の数を返す
    return solutions
# 入力例
n = 4
print(totalNQueens(n))  # 出力: 2
n = 1
print(totalNQueens(n))  # 出力: 1
