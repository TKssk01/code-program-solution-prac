class Solution:
    def calculate(s: str) -> int:
        # スタック、現在の数値、結果、符号を初期化
        stack = []
        current_number = 0
        result = 0
        sign = 1  # 1は正、-1は負を意味する
        
        for char in s:
            if char.isdigit():
                # 数字の場合、current_numberを構築
                current_number = current_number * 10 + int(char)
            elif char == '+':
                # '+'の場合、current_numberを結果に加算し、current_numberをリセット
                result += sign * current_number
                current_number = 0
                sign = 1
            elif char == '-':
                # '-'の場合、current_numberを結果に減算し、current_numberをリセット
                result += sign * current_number
                current_number = 0
                sign = -1
            elif char == '(':
                # '('の場合、現在の結果と符号をスタックに保存し、新しい計算を開始
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            elif char == ')':
                # ')'の場合、current_numberを結果に加算し、スタックから前の結果と符号を取り出して計算を続ける
                result += sign * current_number
                current_number = 0
                result *= stack.pop()  # これは符号
                result += stack.pop()  # これは前の結果
            # 空白は無視
        
        if current_number != 0:
            # 最後の数値を結果に加算
            result += sign * current_number
        
        return result

# テストケース
solution = Solution()
print(solution.calculate("1 + 1"))  # 出力: 2
print(solution.calculate(" 2-1 + 2 "))  # 出力: 3
print(solution.calculate("(1+(4+5+2)-3)+(6+8)"))  # 出力: 23