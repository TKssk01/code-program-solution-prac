from collections import deque
from typing import Optional
from typing import List

# 二分木のノードを表すクラスを定義
class TreeNode:
    # コンストラクタ：値、左の子ノード、右の子ノードを初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解答のためのクラスを定義
class Solution:
    # パスの合計が目標値と一致するかを判定するメソッド
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # ベースケース：ノードが存在しない場合はFalseを返す
        if not root:
            return False
        
        # 葉ノードで、かつ値が目標値と等しい場合はTrueを返す
        if not root.left and not root.right and root.val == targetSum:
            return True
        
        # 左の子ノードと右の子ノードに対して再帰的に処理を行う
        # 目標値から現在のノードの値を引いた値を新しい目標値として渡す
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))

# 与えられた値のリストから二分木を作成する関数
def create_tree(values):
    # 値のリストが空の場合はNoneを返す
    if not values:
        return None
    # ルートノードを作成
    root = TreeNode(values[0])
    # 幅優先探索のためのキューを初期化
    queue = [root]
    i = 1
    # キューが空でない、かつ全ての値を処理していない間ループ
    while queue and i < len(values):
        # キューから次のノードを取り出す
        node = queue.pop(0)
        # 左の子ノードを作成（値がNoneでない場合）
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # 右の子ノードを作成（値がNoneでない場合）
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    # 完成した二分木のルートを返す
    return root

# テストケース1：期待される出力はTrue
root1 = create_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])
solution = Solution()
print(solution.hasPathSum(root1, 22))  # 出力: True

# テストケース2：期待される出力はFalse
root2 = create_tree([1,2,3])
print(solution.hasPathSum(root2, 5))  # 出力: False

# テストケース3：空の木、期待される出力はFalse
root3 = create_tree([])
print(solution.hasPathSum(root3, 0))  # 出力: False
