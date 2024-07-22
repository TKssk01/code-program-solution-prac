# 二分木のノードを表現するクラスの定義
class TreeNode:
    # コンストラクタ：値、左の子、右の子を初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val    # ノードの値
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

# BST（二分探索木）のイテレータを実装するクラス
class BSTIterator:
    # コンストラクタ：BSTのルートを受け取り、イテレータを初期化
    def __init__(self, root: TreeNode):
        # スタックを初期化（中順走査のためのノードを保持）
        self.stack = []
        # ルートから最も左のノードまでをスタックに追加
        self._leftmost_inorder(root)
    
    # 与えられたノードから最も左のノードまでをスタックに追加するヘルパーメソッド
    def _leftmost_inorder(self, root):
        # ノードが存在する限り繰り返す
        while root:
            # 現在のノードをスタックに追加
            self.stack.append(root)
            # 左の子に移動
            root = root.left
    
    # 次の要素を返すメソッド
    def next(self) -> int:
        # スタックの一番上（最後に追加された）ノードを取り出す
        topmost_node = self.stack.pop()
        # 取り出したノードに右の子がある場合
        if topmost_node.right:
            # 右の子とその左の子孫をスタックに追加
            self._leftmost_inorder(topmost_node.right)
        # 取り出したノードの値を返す
        return topmost_node.val
    
    # 次の要素が存在するかどうかを返すメソッド
    def hasNext(self) -> bool:
        # スタックが空でなければTrueを返す（次の要素が存在する）
        return len(self.stack) > 0

# 以下は使用例（コメントアウトされています）
# # ルートノードの作成
# root = TreeNode(7)
# # 左の子ノードの作成
# root.left = TreeNode(3)
# # 右の子ノードの作成
# root.right = TreeNode(15)
# # 右の子の左ノードの作成
# root.right.left = TreeNode(9)
# # 右の子の右ノードの作成
# root.right.right = TreeNode(20)
# 
# # BSTIteratorのインスタンスを作成
# iterator = BSTIterator(root)
# # 次の要素（最小値）を取得して表示
# print(iterator.next())    # 3
# # 次の要素を取得して表示
# print(iterator.next())    # 7
# # 次の要素が存在するか確認
# print(iterator.hasNext()) # True
# # 次の要素を取得して表示
# print(iterator.next())    # 9
# # 次の要素が存在するか確認
# print(iterator.hasNext()) # True
# # 次の要素を取得して表示
# print(iterator.next())    # 15
# # 次の要素が存在するか確認
# print(iterator.hasNext()) # True
# # 次の要素を取得して表示
# print(iterator.next())    # 20
# # 次の要素が存在するか確認
# print(iterator.hasNext()) # False