class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # s1とs2の長さの合計がs3の長さと一致しない場合、Falseを返す
        if len(s1) + len(s2) != len(s3):
            return False
        # DPテーブルを初期化する。サイズは (len(s1) + 1) x (len(s2) + 1)
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
        # 初期条件：空文字列同士ならTrue
        dp[0][0] = True
        # s1の各文字に対して、s3が対応する部分と一致するかをチェックし、DPテーブルを更新
        for i in range(1, len(s1) + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        # s2の各文字に対して、s3が対応する部分と一致するかをチェックし、DPテーブルを更新
        for j in range(1, len(s2) + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        # s1とs2の各部分文字列に対して、s3がインターリーブ可能かどうかをDPテーブルに記録
        for i in range(1, len(s1) + 1):
            for j in range(1, len(s2) + 1):
                # s1のi番目の文字がs3の(i+j)番目と一致する場合、または
                # s2のj番目の文字がs3の(i+j)番目と一致する場合にTrue
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        # 最終的にs1とs2全体でs3が作れるかを返す
        return dp[len(s1)][len(s2)]
