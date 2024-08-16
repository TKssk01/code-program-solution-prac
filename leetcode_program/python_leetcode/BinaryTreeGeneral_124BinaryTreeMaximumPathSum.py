from typing import Optional
# バイナリツリーのノードを定義するクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# 解を求めるためのクラス
class Solution:
    # バイナリツリーの最大経路和を計算する関数
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # 最大経路和を格納する変数を負の無限大で初期化
        self.max_sum = float('-inf')
        # 深さ優先探索 (DFS) を行うヘルパー関数
        def dfs(node):
            # ベースケース: ノードが存在しない場合は0を返す
            if not node:
                return 0
            # 左部分木の最大経路和を計算 (0未満なら切り捨て)
            left_gain = max(dfs(node.left), 0)
            # 右部分木の最大経路和を計算 (0未満なら切り捨て)
            right_gain = max(dfs(node.right), 0)
            # 現在のノードを根とする経路の和を計算
            current_max_path = node.val + left_gain + right_gain
            # グローバルな最大経路和を更新
            self.max_sum = max(self.max_sum, current_max_path)
            # このノードを含む経路で上に返すべき最大の一方向の経路和を返す
            return node.val + max(left_gain, right_gain)
        # ルートノードからDFSを開始
        dfs(root)
        # 最終的な最大経路和を返す
        return self.max_sum