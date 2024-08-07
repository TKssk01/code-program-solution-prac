class Solution:
    def hammingWeight(self, n: int) -> int:
        # 整数をバイナリ文字列に変換し、"0b"のプレフィックスを取り除く
        binary_representation = bin(n)[2:]  # bin() 関数を使って整数をバイナリ文字列に変換し、先頭の "0b" を取り除く
        # バイナリ文字列中の '1' の数を数える
        set_bits_count = binary_representation.count("1")  # バイナリ文字列内の '1' の数を数える
        # セットビットの数を返す
        return set_bits_count  # 数えたセットビットの数を返す
