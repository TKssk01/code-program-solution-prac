from collections import deque
from typing import Optional
from typing import List
# 二分木のノードを表すクラスの定義
class TreeNode:
    # コンストラクタ：値、左の子、右の子を初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 解答のクラス
class Solution:
    # 最小絶対差を求めるメソッド
    def getMinimumDifference(self, root: TreeNode) -> int:
        # 中間順巡回を行う内部関数
        def inorder(node):
            # ノードが存在しない場合は処理を終了
            if not node:
                return
            
            # 左の子ノードを再帰的に処理
            inorder(node.left)
            
            # 前のノードが存在する場合（最初のノード以外）
            if self.prev is not None:
                # 現在のノードと前のノードの差を計算し、最小値を更新
                self.min_diff = min(self.min_diff, node.val - self.prev)
            # 現在のノードの値を前のノードとして記録
            self.prev = node.val
            
            # 右の子ノードを再帰的に処理
            inorder(node.right)
        
        # 前のノードの値を保持する変数を初期化
        self.prev = None
        # 最小差を無限大で初期化
        self.min_diff = float('inf')
        # 中間順巡回を開始
        inorder(root)
        # 計算された最小差を返す
        return self.min_diff