from typing import List
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        s_list = s.split()
        # 文字列 pattern から文字列 s への対応関係を保持する辞書
        if len(s_list) != len(pattern):
            return False
        pattern_to_s = {}
        # 文字列 s から文字列 pattern への対応関係を保持する辞書
        s_to_pattern = {}
        # 文字列 pattern と s を同時に走査し、各文字をペアとして取り出す
        for char_pattern, char_s in zip(pattern, s_list):
            # pattern_to_s に char_pattern が存在し、対応する値が char_s と異なる場合、False を返す
            if char_pattern in pattern_to_s:
                if pattern_to_s[char_pattern] != char_s:
                    return False
            # s_to_pattern に char_s が存在し、対応する値が char_pattern と異なる場合、False を返す
            if char_s in s_to_pattern:
                if s_to_pattern[char_s] != char_pattern:
                    return False

            pattern_to_s[char_pattern] = char_s            
            s_to_pattern[char_s] = char_pattern
            # # char_pattern をキーとして、対応する char_s を pattern_to_s に追加または更新
            # pattern_to_s[char_pattern] = char_s
            # # char_s をキーとして、対応する char_pattern を s_to_pattern に追加または更新
            # s_to_pattern[char_s] = char_pattern
        # 全てのチェックをパスした場合、True を返す
        return True

# テストケース
if __name__ == "__main__":
    solution = Solution()
    pattern = "abba"
    s = "dog cat cat dog"
    print(solution.wordPattern(pattern, s))

    s = "dog cat dog cat"
    pattern = "abba"
    print(solution.wordPattern(pattern, s))  # True

    s = "dog cat fish cat"
    pattern = "abba"
    print(solution.wordPattern(pattern, s))  # False