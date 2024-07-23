from collections import deque
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: TreeNode, k: int) -> int:
    # 中順走査の結果を保存するリスト
    inorder_list = []
    
    # 中順走査を行う再帰関数
    def inorder_traversal(node: TreeNode):
        if node:
            # 左の子ノードを訪問
            inorder_traversal(node.left)
            # 現在のノードをリストに追加
            inorder_list.append(node.val)
            # 右の子ノードを訪問
            inorder_traversal(node.right)
    
    # 中順走査を開始
    inorder_traversal(root)
    
    # k 番目の要素を返す (1-indexed のため k-1)
    return inorder_list[k - 1]

# 例1
root1 = TreeNode(3)
root1.left = TreeNode(1)
root1.right = TreeNode(4)
root1.left.right = TreeNode(2)

print(kthSmallest(root1, 1))  # 出力: 1

# 例2
root2 = TreeNode(5)
root2.left = TreeNode(3)
root2.right = TreeNode(6)
root2.left.left = TreeNode(2)
root2.left.right = TreeNode(4)
root2.left.left.left = TreeNode(1)

print(kthSmallest(root2, 3))  # 出力: 3
