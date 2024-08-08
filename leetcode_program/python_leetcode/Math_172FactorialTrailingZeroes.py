class Solution:
    def trailingZeroes(self, n: int) -> int:
        # 末尾のゼロのカウントを初期化する
        zero_sum = 0
        # nが0より大きい間ループを続ける
        while n > 0:
            # nを5で割り、その商をnに代入する
            n //= 5
            # 商をzero_sumに加算する
            zero_sum += n
        # 累積した末尾のゼロの数を返す
        return zero_sum
# 実行例
if __name__ == "__main__":
    solution = Solution()    
    # 例1: n = 3
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {solution.trailingZeroes(n)}")  # 出力: 0
    # 例2: n = 5
    n = 5
    print(f"Input: n = {n}")
    print(f"Output: {solution.trailingZeroes(n)}")  # 出力: 1
    # 例3: n = 0
    n = 0
    print(f"Input: n = {n}")
    print(f"Output: {solution.trailingZeroes(n)}")  # 出力: 0
    # 追加の例: n = 100
    n = 100
    print(f"Input: n = {n}")
    print(f"Output: {solution.trailingZeroes(n)}")  # 出力: 24
