from collections import Counter

def findSubstring(s, words):
    # 各単語の長さ
    word_len = len(words[0])
    # 全体の長さ
    total_len = word_len * len(words)
    # 結果のインデックスを保存するリスト
    result = []
    # wordsの出現回数をカウント
    words_count = Counter(words)    
    # sの中の全ての部分文字列を確認
    for i in range(len(s) - total_len + 1):
        # 対象の部分文字列
        substring = s[i:i+total_len]
        # 部分文字列をword_lenごとに分割してカウント
        seen = []
        for j in range(0, total_len, word_len):
            part = substring[j:j+word_len]
            seen.append(part)
        # wordsの出現回数と部分文字列の出現回数が一致するか確認
        if Counter(seen) == words_count:
            result.append(i)
    return result
# テストケース
s1 = "barfoothefoobarman"
words1 = ["foo","bar"]
print(findSubstring(s1, words1))  # 出力: [0, 9]
s2 = "wordgoodgoodgoodbestword"
words2 = ["word","good","best","word"]
print(findSubstring(s2, words2))  # 出力: []
s3 = "barfoofoobarthefoobarman"
words3 = ["bar","foo","the"]
print(findSubstring(s3, words3))  # 出力: [6, 9, 12]