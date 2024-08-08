class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # シフトした回数をカウントする変数
        shift_count = 0
        # left が right より小さい間ループを回す
        while left < right:
            # left を1ビット右シフトする
            left >>= 1
            # right を1ビット右シフトする
            right >>= 1
            # シフト回数をインクリメントする
            shift_count += 1
        # 共通ビット部分を元の位置に戻すために左シフトする
        return left << shift_count
