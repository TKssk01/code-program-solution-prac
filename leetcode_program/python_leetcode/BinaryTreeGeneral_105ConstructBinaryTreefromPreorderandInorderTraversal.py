from typing import List, Optional
# TreeNodeの定義
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値を初期化
        self.left = left  # 左の子ノードを初期化
        self.right = right  # 右の子ノードを初期化
# Solutionクラスの定義
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # ベースケース: preorder または inorder が空の場合、None を返す
        if not preorder or not inorder:
            return None
        # preorderの最初の値がルートノードの値となる
        root_val = preorder[0]
        # ルートノードを作成
        root = TreeNode(root_val)
        # inorder配列でルートノードの値のインデックスを見つける
        mid = inorder.index(root_val)
        # 左部分木を再帰的に構築
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        # 右部分木を再帰的に構築
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        # 構築したツリーのルートノードを返す
        return root
# テストデータを定義
preorder = [3, 9, 20, 15, 7]
inorder = [9, 3, 15, 20, 7]
# Solutionクラスのインスタンスを作成
solution = Solution()
# ツリーを構築
root = solution.buildTree(preorder, inorder)
# ツリーを表示するための補助関数
def printTree(node):
    if not node:
        return None
