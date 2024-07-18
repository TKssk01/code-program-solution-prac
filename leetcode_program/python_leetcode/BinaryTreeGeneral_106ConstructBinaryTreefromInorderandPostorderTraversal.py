from typing import List, Optional
# TreeNode クラスの定義（与えられたもの）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # inorder または postorder が空の場合、None を返す
        if not inorder or not postorder:
            return None
        # postorder の最後の要素を取得し、これが根の値となる
        root_val = postorder.pop()
        # 新しい TreeNode を作成し、その値を root_val に設定する
        root = TreeNode(root_val)
        # inorder 配列で root_val のインデックスを見つける
        inorder_index = inorder.index(root_val)
        # 再帰的に右部分木を構築
        root.right = self.buildTree(inorder[inorder_index+1:], postorder)
        # 再帰的に左部分木を構築
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        # 構築されたツリーの根を返す
        return root
