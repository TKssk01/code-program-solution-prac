class Trie:
    def __init__(self):
        # トライのルートを空の辞書で初期化し、終端フラグを持たせる
        self.root = {"#": False}

    def insert(self, word):
        # ルートからスタート
        node = self.root
        # 挿入する文字列の各文字についてループ
        for char in word:
            # 子ノードに文字が存在しない場合、新しい辞書を作成
            if char not in node:
                node[char] = {"#": False}
            # 子ノードに進む
            node = node[char]
        # 最後のノードを単語の終端としてマーク
        node["#"] = True

    def search(self, word):
        # ルートからスタート
        node = self.root
        # 検索する文字列の各文字についてループ
        for char in word:
            # 子ノードに文字が存在しない場合、単語は存在しない
            if char not in node:
                return False
            # 子ノードに進む
            node = node[char]
        # 最後のノードが単語の終端であるかを返す
        return node.get("#", False)

    def startsWith(self, prefix):
        # ルートからスタート
        node = self.root
        # プレフィックスの各文字についてループ
        for char in prefix:
            # 子ノードに文字が存在しない場合、プレフィックスは存在しない
            if char not in node:
                return False
            # 子ノードに進む
            node = node[char]
        # プレフィックスが存在する場合はTrueを返す
        return True
