from collections import deque
from typing import Optional
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # ベースケース：ルートが空またはリーフノードの場合
        if not root or (not root.left and not root.right):
            return root
        # 左部分木を平坦化
        left_tail = self.flatten(root.left)
        # 右部分木を平坦化
        right_tail = self.flatten(root.right)
        # 左部分木が存在する場合
        if left_tail:
            # 左部分木の末尾を元の右部分木につなぐ
            left_tail.right = root.right
            # ルートの右をルートの左につなぐ
            root.right = root.left
            # ルートの左を None にする
            root.left = None
        # 末尾ノードを返す（右部分木がある場合はその末尾、なければ左部分木の末尾、どちらもなければルート）
        return right_tail or left_tail or root
# テスト用のヘルパー関数
def create_tree(values):
    if not values:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    return root

def print_flattened_tree(root):
    result = []
    while root:
        result.append(root.val)
        root = root.right
    print(result)

# テスト
sol = Solution()
# Example 1
root1 = create_tree([1,2,5,3,4,None,6])
sol.flatten(root1)
print_flattened_tree(root1)  # [1, 2, 3, 4, 5, 6]
# Example 2
root2 = create_tree([])
sol.flatten(root2)
print_flattened_tree(root2)  # []
# Example 3
root3 = create_tree([0])
sol.flatten(root3)
print_flattened_tree(root3)  # [0]