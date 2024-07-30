# 必要なライブラリのインポート
from typing import List
# ソリューションクラスを定義
class Solution:
    # nペアの括弧の組み合わせを生成する関数を定義
    def generateParenthesis(self, n: int) -> List[str]:
        # バックトラック関数を定義。currentは現在の括弧の組み合わせ、openは開いた括弧の数、closeは閉じた括弧の数、resultは結果リスト
        def backtrack(current, open, close, result):
            # 現在の括弧の組み合わせの長さが2 * nになったら、それを結果リストに追加して終了
            if len(current) == 2 * n:
                result.append(current)
                return
            # 開いた括弧の数がnより小さい場合、新しい開く括弧を追加して再帰呼び出し
            if open < n:
                backtrack(current + "(", open + 1, close, result)
            # 閉じた括弧の数が開いた括弧の数より少ない場合、新しい閉じる括弧を追加して再帰呼び出し
            if close < open:
                backtrack(current + ")", open, close + 1, result)
        # 結果を格納するリストを初期化
        result = []
        # 最初は空の文字列、開いた括弧と閉じた括弧の数が0の状態でバックトラック関数を呼び出す
        backtrack("", 0, 0, result)
        # 結果リストを返す
        return result
# テストの例
sol = Solution()
print(sol.generateParenthesis(3))  # ["((()))","(()())","(())()","()(())","()()()"]
print(sol.generateParenthesis(1))  # ["()"]
