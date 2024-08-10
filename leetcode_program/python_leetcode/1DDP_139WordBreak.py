from typing import List
class WordBreaker:
    def __init__(self, wordDict: List[str]):
        # 単語辞書をインスタンス変数に保存
        self.wordDict = wordDict    
    def wordBreak(self, s: str) -> bool:
        # sの長さ+1のFalseで初期化されたリストを作成
        dp = [False] * (len(s) + 1)
        # dp[0]をTrueに設定（空文字列は常に分割可能と見なす）
        dp[0] = True
        # sの各部分文字列について処理を行うループ
        for i in range(1, len(s) + 1):
            # i文字目までのsを、さらに細かい部分に分割してチェックするループ
            for j in range(i):
                # sのj番目までが分割可能であり、かつs[j:i]がwordDictに含まれる場合
                if dp[j] and s[j:i] in self.wordDict:
                    # dp[i]をTrueに設定し、分割可能であるとマークする
                    dp[i] = True
                    # Trueになった時点で他のjについての検証を止める
                    break
        # s全体が分割可能かどうかの結果を返す
        return dp[len(s)]
# テストケース
wordDict1 = ["leet", "code"]
wb1 = WordBreaker(wordDict1)
s1 = "leetcode"
print(wb1.wordBreak(s1))  # True
wordDict2 = ["apple", "pen"]
wb2 = WordBreaker(wordDict2)
s2 = "applepenapple"
print(wb2.wordBreak(s2))  # True
wordDict3 = ["cats", "dog", "sand", "and", "cat"]
wb3 = WordBreaker(wordDict3)
s3 = "catsandog"
print(wb3.wordBreak(s3))  # False