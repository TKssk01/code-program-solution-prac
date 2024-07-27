# Trieノードを表すクラス
class TrieNode:
    def __init__(self):
        # 各ノードが持つ子ノードを格納する辞書
        self.children = {}
        # 単語の終端を示すフラグ
        self.is_end_of_word = False

# WordDictionaryクラスを定義
class WordDictionary:
    def __init__(self):
        # ルートノードを初期化
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        # 現在のノードをルートに設定
        node = self.root
        # 単語の各文字を処理
        for char in word:
            # 子ノードが存在しない場合は新しいTrieNodeを作成
            if char not in node.children:
                node.children[char] = TrieNode()
            # 次のノードに移動
            node = node.children[char]
        # 単語の終端に到達したことを示すフラグを設定
        node.is_end_of_word = True

    def search(self, word: str) -> bool:
        # 内部関数を定義して再帰的に検索
        def search_in_node(word, node):
            # 単語の各文字を処理
            for i, char in enumerate(word):
                # ドットの場合はすべての子ノードを探索
                if char == '.':
                    for x in node.children.values():
                        if search_in_node(word[i+1:], x):
                            return True
                    return False
                else:
                    # 子ノードが存在しない場合はFalseを返す
                    if char not in node.children:
                        return False
                    # 次のノードに移動
                    node = node.children[char]
            # 単語の終端に到達した場合はTrueを返す
            return node.is_end_of_word

        # ルートノードから検索を開始
        return search_in_node(word, self.root)
