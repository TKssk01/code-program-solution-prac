from collections import deque
from typing import Optional
from typing import List
# 二分木のノードを表すクラス定義（コメントアウトされている）
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# ソリューションクラスの定義
class Solution:
    # ジグザグレベルオーダートラバーサルを行うメソッド
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # ルートが存在しない場合、空のリストを返す
        if not root:
            return []
        # 結果を格納するリストを初期化
        result = []

        # ノードを一時的に格納するキューを初期化し、ルートノードを追加
        queue = deque([root])
        # 左から右への走査フラグを初期化
        left_to_right = True

        # キューが空になるまでループ
        while queue:
            # 現在のレベルのノード数を取得
            level_size = len(queue)
            # 現在のレベルのノード値を格納するリストを初期化
            level = []

            # 現在のレベルのすべてのノードを処理
            for _ in range(level_size):
                # 左から右への走査の場合
                if left_to_right:
                    # キューの左側からノードを取り出す
                    node = queue.popleft()
                    # ノードの値をレベルリストに追加
                    level.append(node.val)
                    # 左子ノードが存在する場合、キューに追加
                    if node.left:
                        queue.append(node.left)
                    # 右子ノードが存在する場合、キューに追加
                    if node.right:
                        queue.append(node.right)
                # 右から左への走査の場合
                else:
                    # キューの右側からノードを取り出す
                    node = queue.pop()
                    # ノードの値をレベルリストに追加
                    level.append(node.val)
                    # 右子ノードが存在する場合、キューの左側に追加
                    if node.right:
                        queue.appendleft(node.right)
                    # 左子ノードが存在する場合、キューの左側に追加
                    if node.left:
                        queue.appendleft(node.left)

            # 現在のレベルの結果をresultリストに追加
            result.append(level)
            # 次のレベルの走査方向を反転
            left_to_right = not left_to_right

        # 最終結果を返す
        return result