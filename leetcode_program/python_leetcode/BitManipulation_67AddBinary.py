class Solution:
    def addBinary(self, a: str, b: str) -> str:
        max_len = max(len(a), len(b))

        # 長さを揃えるためにゼロ埋めします
        a = a.zfill(max_len)
        b = b.zfill(max_len)

        # 結果を保持する変数
        result = []
        carry = 0

        # 右から左へループします
        for i in range(max_len - 1, -1, -1):
            total_sum = int(a[i]) + int(b[i]) + carry
            carry = total_sum // 2
            result.append(str(total_sum % 2))

        # 最後にキャリーが残っている場合、それを追加します
        if carry != 0:
            result.append(str(carry))

        # 結果を逆順にして結合します
        return ''.join(result[::-1])
                
                
            
        