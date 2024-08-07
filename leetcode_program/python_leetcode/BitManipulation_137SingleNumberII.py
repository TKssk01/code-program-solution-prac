from typing import List
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # ビットごとのカウントを初期化
        bits = [0] * 32
        # 各数字に対して、各ビット位置の1の出現回数をカウント
        for num in nums:
            for i in range(32):
                bits[i] += (num >> i) & 1
        # 結果を初期化
        result = 0
        # 各ビット位置について、出現回数を3で割った余りを使って結果を作成
        for i in range(32):
            if bits[i] % 3 != 0:
                # 符号ビット（32ビット目）の処理
                if i == 31:
                    result -= (1 << i)
                else:
                    # 他のビット位置の処理
                    result |= (1 << i)
        # 一度だけ出現する要素を返す
        return result
