class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 入力文字列が空であれば、空文字列を返す
        if len(s) == 0:
            return ""
        # 最長回文部分文字列の開始位置と終了位置を初期化
        start, end = 0, 0
        # 中心を指定して回文を拡張する関数
        def expandAroundCenter(left: int, right: int) -> int:
            # 左右が文字列の範囲内にあり、かつ文字が同じである間、拡張を続ける
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1  # 左側をさらに広げる
                right += 1  # 右側をさらに広げる
            # 最後に回文の長さを返す（right - left - 1 は正しい回文長）
            return right - left - 1
        # 文字列の各文字を中心にしてループ
        for i in range(len(s)):
            # 中心が1文字の場合の回文の長さを計算
            len1 = expandAroundCenter(i, i)
            # 中心が2文字の場合の回文の長さを計算
            len2 = expandAroundCenter(i, i + 1)
            # どちらの回文が長いかを決定
            max_len = max(len1, len2)
            # これまでに見つかった最大の回文よりも長ければ、開始と終了位置を更新
            if max_len > end - start:
                start = i - (max_len - 1) // 2  # 新しい開始位置を計算
                end = i + max_len // 2  # 新しい終了位置を計算
        # 最長回文部分文字列を返す
        return s[start:end + 1]
