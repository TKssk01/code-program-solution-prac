from typing import Optional
# 二分木のノードを表すクラスを定義
class TreeNode:
    # コンストラクタ：ノードの値と左右の子ノードを初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

# 問題を解くためのクラスを定義
class Solution:
    # 二分木の根から葉までのパスが表す数の合計を計算するメソッド
    def sumNumbers(self, root: TreeNode) -> int:
        # 深さ優先探索（DFS）を行う内部関数を定義
        def dfs(node: TreeNode, current_sum: int) -> int:
            # ベースケース：ノードが存在しない場合は0を返す
            if not node:
                return 0
            
            # 現在のノードの値を加える（10倍して現在の値を加えることで桁を正しく扱う）
            current_sum = current_sum * 10 + node.val
            
            # 葉ノードの場合、現在の合計を返す
            if not node.left and not node.right:
                return current_sum
            
            # 左右の子ノードを再帰的に探索し、結果を合計する
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # DFSを開始し、結果を返す
        return dfs(root, 0)

# テストケースを実行する関数
def test_sum_numbers():
    # テストケース1: [1,2,3]
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    # テストケース1の結果を検証
    assert Solution().sumNumbers(root1) == 25

    # テストケース2: [4,9,0,5,1]
    root2 = TreeNode(4)
    root2.left = TreeNode(9)
    root2.right = TreeNode(0)
    root2.left.left = TreeNode(5)
    root2.left.right = TreeNode(1)
    # テストケース2の結果を検証
    assert Solution().sumNumbers(root2) == 1026

    # すべてのテストケースが成功したことを表示
    print("All test cases passed!")

# テストを実行
test_sum_numbers()