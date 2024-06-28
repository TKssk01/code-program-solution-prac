class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 文字列の前後の空白を削除
        s = s.strip()
        # 2. 文字列をスペースで分割して単語のリストを取得
        words = s.split()
        # 3. 単語のリストを逆にする
        words.reverse()
        # 4. 単語を一つのスペースで連結して新しい文字列を作成
        return ' '.join(words)