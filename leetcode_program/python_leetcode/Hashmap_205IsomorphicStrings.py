class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 文字列 s と t の長さが異なる場合、False を返す
        if len(s) != len(t):
            return False
        # 文字列 s から文字列 t への対応関係を保持する辞書
        s_to_t = {}
        # 文字列 t から文字列 s への対応関係を保持する辞書
        t_to_s = {}
        # 文字列 s と t を同時に走査し、各文字をペアとして取り出す
        for char_s, char_t in zip(s, t):
            # s_to_t に char_s が存在し、対応する値が char_t と異なる場合、False を返す
            if char_s in s_to_t and s_to_t[char_s] != char_t:
                return False
            # t_to_s に char_t が存在し、対応する値が char_s と異なる場合、False を返す
            if char_t in t_to_s and t_to_s[char_t] != char_s:
                return False
            # char_s をキーとして、対応する char_t を s_to_t に追加または更新
            s_to_t[char_s] = char_t
            # char_t をキーとして、対応する char_s を t_to_s に追加または更新
            t_to_s[char_t] = char_s
        # 全てのチェックをパスした場合、True を返す
        return True


# def is_isomorphic(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
    
#     s_to_t = {}
#     t_to_s = {}
    
#     for c1, c2 in zip(s, t):
#         if c1 not in s_to_t and c2 not in t_to_s:
#             s_to_t[c1] = c2
#             t_to_s[c2] = c1
#         elif s_to_t.get(c1) != c2 or t_to_s.get(c2) != c1:
#             return False
    
#     return True