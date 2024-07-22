# collections モジュールから deque をインポート（効率的なキュー操作のため）
from collections import deque
from typing import List
# 二分木のノードを表現するクラスを定義
class TreeNode:
    # ノードの初期化メソッド
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノード
        self.right = right  # 右の子ノード
# レベルオーダートラバーサルを行うクラス
class Solution:
    # レベルオーダートラバーサルを実行するメソッド
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # ルートが存在しない場合、空リストを返す
        if not root:
            return []
        # 結果を格納するリストを初期化
        result = []
        # キューを初期化し、ルートノードを追加
        queue = deque([root])
        # キューが空になるまでループ
        while queue:
            # 現在のレベルのノード数を取得
            level_size = len(queue)
            # 現在のレベルのノードの値を格納するリスト
            current_level = []
            # 現在のレベルのすべてのノードを処理
            for _ in range(level_size):
                # キューから次のノードを取り出す
                node = queue.popleft()
                # ノードの値を現在のレベルリストに追加
                current_level.append(node.val)
                # 左の子ノードがあれば、キューに追加
                if node.left:
                    queue.append(node.left)
                # 右の子ノードがあれば、キューに追加
                if node.right:
                    queue.append(node.right)
            # 現在のレベルのリストを結果リストに追加
            result.append(current_level)
        # 完成したレベルオーダートラバーサルの結果を返す
        return result
# 使用例
# ルートノードを作成
root = TreeNode(3)
# 左の子ノードを追加
root.left = TreeNode(9)
# 右の子ノードを追加
root.right = TreeNode(20)
# 右の子の左ノードを追加
root.right.left = TreeNode(15)
# 右の子の右ノードを追加
root.right.right = TreeNode(7)
# Solutionクラスのインスタンスを作成
solution = Solution()
# レベルオーダートラバーサルを実行し、結果を出力
print(solution.levelOrder(root))  # 出力: [[3], [9, 20], [15, 7]]