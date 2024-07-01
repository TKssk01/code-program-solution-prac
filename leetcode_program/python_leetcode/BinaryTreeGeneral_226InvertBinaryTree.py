from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return None
        # 左右の子ノードを入れ替え
        root.left, root.right = root.right, root.left
        # 左の子ノードを反転
        self.invertTree(root.left)
        # 右の子ノードを反転
        self.invertTree(root.right)
        return root