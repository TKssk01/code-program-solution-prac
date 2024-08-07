class Solution:
    def reverseBits(self, n: int) -> int:
        # 結果を格納する変数を0に初期化する
        result = 0
        # 32回ループして各ビットを処理する
        for i in range(32):
            # nを右にiビットシフトし、最下位ビットを取得する
            bit = (n >> i) & 1
            # 取得したビットを結果の反転位置にシフトして追加する
            result = result | (bit << (31 - i))
        # 反転した結果を返す
        return result
