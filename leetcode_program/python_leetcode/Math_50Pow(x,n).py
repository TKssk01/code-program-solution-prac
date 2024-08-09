class Solution:
    def myPow(self, x: float, n: int) -> float:
        # n が 0 の場合、結果は常に 1
        if n == 0:
            return 1
        # n が負の数の場合、x を反転させ、n を正にする
        elif n < 0:
            x = 1 / x
            n = -n
        # 結果を格納する変数を 1 に初期化
        result = 1
        # n が 0 になるまでループを続ける
        while n:
            # n が奇数の場合、現在の x を result に掛ける
            if n % 2:  # n が奇数の場合
                result *= x
            # x を 2 乗する
            x *= x  # x を2乗 ここで、x^nが両方とも増えていくため、この式で条件を満たすことができる
            # n を半分にする（整数の割り算）
            n //= 2  # n を半分に
        # 最終的な結果を返す
        return result
