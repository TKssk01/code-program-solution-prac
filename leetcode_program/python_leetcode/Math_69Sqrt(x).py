class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
    
        # 初期推定値を x の半分に設定する
        guess = x / 2
        while True:
            # 新しい推定値を計算する
            new_guess = (guess + x / guess) / 2.0
            # 新しい推定値と前の推定値の差が非常に小さくなったら収束とみなし、整数に変換して返す
            if abs(new_guess - guess) < 1e-10:
                return int(new_guess)
            # 新しい推定値を次の反復の推定値として設定する
            guess = new_guess