from collections import deque
from typing import Optional
from typing import List
# TreeNodeクラスの定義
class TreeNode:
    # TreeNodeクラスのコンストラクタ。ノードの値、左部分木、右部分木を初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# BSTかどうかを判定する関数
def isValidBST(root):
    # 内部ヘルパー関数の定義。現在のノードがBSTの条件を満たしているか確認する
    def helper(node, lower=float('-inf'), upper=float('inf')):
        # ノードが存在しない場合はTrue（再帰の終了条件）
        if not node:
            return True
        # 現在のノードの値を取得
        val = node.val
        # ノードの値が許容範囲内にあるか確認
        if val <= lower or val >= upper:
            return False
        # 右部分木が有効か確認。現在のノードの値を下限として渡す
        if not helper(node.right, val, upper):
            return False
        # 左部分木が有効か確認。現在のノードの値を上限として渡す
        if not helper(node.left, lower, val):
            return False
        # 現在のノードが条件を満たしていればTrueを返す
        return True
    # ヘルパー関数を呼び出し、ルートノードからチェックを開始
    return helper(root)
# テストケース1: 木構造 [2, 1, 3]
root1 = TreeNode(2)
root1.left = TreeNode(1)
root1.right = TreeNode(3)
# 出力: True
print(isValidBST(root1))

# テストケース2: 木構造 [5, 1, 4, null, null, 3, 6]
root2 = TreeNode(5)
root2.left = TreeNode(1)
root2.right = TreeNode(4)
root2.right.left = TreeNode(3)
root2.right.right = TreeNode(6)
# 出力: False
print(isValidBST(root2))
