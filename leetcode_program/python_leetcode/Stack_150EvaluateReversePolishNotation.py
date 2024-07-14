from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []  # スタックを初期化
        for token in tokens:
            if token in '+-*/':
                # トークンが演算子の場合、スタックから2つのオペランドをポップ
                b = stack.pop()
                a = stack.pop()
                # 演算子に応じて計算を実行し、結果をスタックにプッシュ
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    # Pythonの//は符号を無視した切り捨て除算を行うので、intでキャストして調整する
                    stack.append(int(a / b))
            else:
                # トークンが数字の場合、整数に変換してスタックにプッシュ
                stack.append(int(token))

        # 最後にスタックに残った唯一の値が計算結果
        return stack[0]

# インスタンス作成
solution = Solution()

# テスト例
tokens1 = ["2", "1", "+", "3", "*"]
print(solution.evalRPN(tokens1))  # 出力: 9

tokens2 = ["4", "13", "5", "/", "+"]
print(solution.evalRPN(tokens2))  # 出力: 6

tokens3 = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
print(solution.evalRPN(tokens3))  # 出力: 22
