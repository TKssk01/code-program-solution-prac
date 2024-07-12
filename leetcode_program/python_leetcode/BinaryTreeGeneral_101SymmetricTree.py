# Definition for a binary tree node.
# 二分木のノードを定義します。
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # 二つのサブツリーが対称かどうかをチェックするヘルパー関数を定義します。
        def isMirror(left: TreeNode, right: TreeNode) -> bool:
            # 両方のサブツリーが空の場合、それらは対称です。
            if not left and not right:
                return True
            # 一方のみが空の場合、それらは対称ではありません。
            if not left or not right:
                return False
            # 両方のノードの値が同じであり、それぞれの子ノードが対称であるかを再帰的にチェックします。
            return (left.val == right.val) and isMirror(left.left, right.right) and isMirror(left.right, right.left)
        # 根が空の場合、それは対称です。
        if not root:
            return True
        # 根の左と右のサブツリーが対称かどうかをチェックします。
        return isMirror(root.left, root.right)