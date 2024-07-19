# Definition for a binary tree node.
from collections import deque
from typing import Optional
from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # ルートノードがNone（空の木）であれば、空のリストを返す
        if not root:
            return []
        
        result = []  # 各レベルの平均値を格納するためのリストを初期化
        queue = deque([root])  # 幅優先探索のためのキューを初期化し、ルートノードを追加する
        
        # キューが空になるまで処理を続ける
        while queue:
            level_length = len(queue)  # 現在のレベルにあるノードの数を取得する
            level_sum = 0  # 現在のレベルのノードの値の合計を初期化する
            
            # 現在のレベルにある各ノードを処理する
            for _ in range(level_length):
                node = queue.popleft()  # キューの先頭からノードを取り出す
                level_sum += node.val  # ノードの値をレベルの合計に追加する
                
                # 左の子ノードが存在する場合、キューに追加する
                if node.left:
                    queue.append(node.left)
                # 右の子ノードが存在する場合、キューに追加する
                if node.right:
                    queue.append(node.right)
            
            # 現在のレベルの平均値を計算し、結果リストに追加する
            average = level_sum / level_length
            result.append(average)
        
        return result  # 各レベルの平均値のリストを返す

# 例1のテスト用の木構造を作成
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20)
root1.right.left = TreeNode(15)
root1.right.right = TreeNode(7)

# 例2のテスト用の木構造を作成
root2 = TreeNode(3)
root2.left = TreeNode(9)
root2.right = TreeNode(20)
root2.left.left = TreeNode(15)
root2.left.right = TreeNode(7)

solution = Solution()

# 関数を呼び出して結果を表示
print(solution.averageOfLevels(root1))  # 期待される出力: [3.0, 14.5, 11.0]
print(solution.averageOfLevels(root2))  # 期待される出力: [3.0, 14.5, 11.0]