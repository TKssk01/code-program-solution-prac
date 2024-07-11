class Solution:
    def isValid(self, s: str) -> bool:
        # 対応する括弧のマップを定義
        bracket_map = {')': '(', ']': '[', '}': '{'}
        # スタックを初期化
        stack = []
        # 入力文字列を一文字ずつ走査
        for char in s:
            # もし文字が閉じ括弧であるなら
            if char in bracket_map:
                # スタックが空でなければトップの要素を取り出し、空ならダミー値 '#' を使用
                top_element = stack.pop() if stack else '#'
                # トップの要素が対応する開き括弧でないなら False を返す
                if top_element != bracket_map[char]:
                    return False
            else:
                # 文字が開き括弧ならスタックに追加
                stack.append(char)
        # スタックが空なら全ての括弧が正しく閉じられているので True を返す
        return not stack
