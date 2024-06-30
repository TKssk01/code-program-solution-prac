class Solution:
    def isHappy(self, n: int) -> bool:
        # 各桁の2乗の和を計算する補助関数
        def sum_digits(n):
            return sum(int(digit) ** 2 for digit in str(n))
        # 既に出現した数を記録するセット
        seen = set()
        # nが1になるか、既に出現した数になるまでループを続ける
        while n != 1 and n not in seen:
            seen.add(n)  # 現在の数をセットに追加
            n = sum_digits(n)  # 各桁の2乗の和を計算し、nに再代入
        # nが1ならハッピーナンバー、それ以外はハッピーナンバーではない
        return n == 1