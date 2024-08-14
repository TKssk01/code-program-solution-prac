from typing import List

class Solution:
    # このメソッドは、盤面(board)上で指定された単語(words)を検索し、見つかった単語をリストで返す
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Trieの各ノードを表すクラスを定義する
        class TrieNode:
            def __init__(self):
                self.children = {}  # 子ノードを格納する辞書
                self.end_of_word = False  # 単語の終端を示すフラグ
        # Trieデータ構造を管理するクラスを定義する
        class Trie:
            def __init__(self):
                self.root = TrieNode()  # トライのルートノードを初期化
            # 単語をTrieに挿入するメソッド
            def insert(self, word):
                node = self.root  # ルートノードから開始
                for char in word:  # 単語の各文字を処理
                    if char not in node.children:  # 子ノードに文字が存在しなければ
                        node.children[char] = TrieNode()  # 新しいノードを追加
                    node = node.children[char]  # ノードを進める
                node.end_of_word = True  # 単語の終端を示すフラグを立てる
        # Trieに単語を挿入する
        trie = Trie()
        for word in words:
            trie.insert(word)
        # 深さ優先探索を行うためのヘルパー関数
        def dfs(node, i, j, path, result):
            # ノードが単語の終端を示す場合、結果リストに単語を追加
            if node.end_of_word:
                result.add(path)
                node.end_of_word = False  # 同じ単語が複数回追加されるのを防ぐためにリセット
            # 盤面の範囲外に出たり、既に訪問済みのセルに移動した場合、探索を終了する
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] == "#":
                return
            # 現在のセルの文字を取得
            tmp = board[i][j]
            # 次のノードに移動できるか確認（トライに該当する子ノードがあるか）
            node = node.children.get(tmp)
            if not node:  # 子ノードがなければ探索を終了
                return
            board[i][j] = "#"  # 現在のセルを訪問済みとしてマーク
            # 4方向（上下左右）に対してDFSを再帰的に実行
            dfs(node, i + 1, j, path + tmp, result)
            dfs(node, i - 1, j, path + tmp, result)
            dfs(node, i, j + 1, path + tmp, result)
            dfs(node, i, j - 1, path + tmp, result)
            board[i][j] = tmp  # 探索が終わったら元の状態に戻す
        result = set()  # 見つかった単語を格納するセット（重複を防ぐため）
        # 盤面の全てのセルを開始点として探索する
        for i in range(len(board)):
            for j in range(len(board[0])):
                dfs(trie.root, i, j, "", result)
        return list(result)  # 結果をリストに変換して返す