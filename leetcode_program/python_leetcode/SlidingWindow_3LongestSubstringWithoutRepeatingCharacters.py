class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 各文字の最新のインデックスを保持する辞書
        char_index_map = {}
        # 現在の部分文字列の開始位置
        left = 0
        # 最長の部分文字列の長さを保持する変数
        max_length = 0
        # 文字列全体を右から左にスキャンする
        for right in range(len(s)):
            # もし現在の文字が既に辞書に存在する場合
            if s[right] in char_index_map:
                # leftポインタを更新して重複を取り除く
                left = max(left, char_index_map[s[right]] + 1)
            # 現在の文字のインデックスを辞書に更新
            char_index_map[s[right]] = right
            # 現在の部分文字列の長さを計算し、最大値を更新
            max_length = max(max_length, right - left + 1)
        return max_length