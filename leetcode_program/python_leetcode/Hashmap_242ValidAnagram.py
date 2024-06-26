class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word_list = {}
        # 一つ目の文字列を辞書に格納する関数
        for char in s:
            if char in word_list:
                word_list[char] += 1
            else:
                word_list[char] = 1
        # 二つ目の文字列がすべて対応しているか確認する関数        
        for char in t:
            if char not in word_list or word_list[char] == 0:
                return False
            word_list[char] -= 1
        # 辞書のすべての要素が空かどうかを確認する関数
        for value in word_list.values():  
            if value != 0:
                return False
        return True
