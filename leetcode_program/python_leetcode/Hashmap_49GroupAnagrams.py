from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 空の辞書を作成。キーはソートされた文字列、値はそのアナグラムのリスト。
        anagrams = {}
        # 入力された文字列のリストを一つずつ処理する。
        for s in strs:
            # 文字列をソートし、ソートされた文字列を作成する。
            # 例えば "eat" は "aet" に、"tea" も "aet" になる。
            sorted_str = ''.join(sorted(s))
            # ソートされた文字列が辞書に存在しない場合、新しいキーとして初期化する。
            if sorted_str not in anagrams:
                anagrams[sorted_str] = []
            # ソートされた文字列をキーに、元の文字列をリストに追加する。
            anagrams[sorted_str].append(s)
        # 辞書の値（アナグラムのリスト）をリストとして返す。
        return list(anagrams.values())