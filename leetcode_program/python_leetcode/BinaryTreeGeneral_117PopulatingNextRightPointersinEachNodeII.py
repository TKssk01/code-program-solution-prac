from typing import Optional
# 二分木のノードを表すクラス
class Node:
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val      # ノードの値
        self.left = left    # 左の子ノード
        self.right = right  # 右の子ノード
        self.next = next    # 次の右側のノード

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        # 根ノードが存在しない場合は処理不要
        if not root:
            return None

        # 現在のレベルの最初のノード
        level_start = root

        # 次のレベルが存在する限り処理を続ける
        while level_start:
            current = level_start
            dummy = Node(0)  # 次のレベルのノードを繋ぐための仮想ノード
            temp = dummy     # 次のレベルのノードを繋ぐ際に使用する一時的なポインタ

            # 現在のレベルのノードを順に処理
            while current:
                # 左の子ノードが存在する場合、次のレベルに追加
                if current.left:
                    temp.next = current.left
                    temp = temp.next

                # 右の子ノードが存在する場合、次のレベルに追加
                if current.right:
                    temp.next = current.right
                    temp = temp.next

                # 現在のレベルの次のノードへ移動
                current = current.next

            # 次のレベルの最初のノードに移動
            level_start = dummy.next

        return root

# 結果を表示するための関数
def print_next_pointers(root):
    result = []
    level_start = root

    # 全てのレベルを処理
    while level_start:
        current = level_start
        # 現在のレベルのノードを処理
        while current:
            result.append(str(current.val))
            current = current.next
        result.append('#')  # レベルの終わりを示す
        # 次のレベルの最初のノードを探す
        level_start = level_start.left or level_start.right

    return result

# テスト用の二分木を作成
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(7)

# nextポインタを設定
solution = Solution()
connected_root = solution.connect(root)

# 結果を表示
print(print_next_pointers(connected_root))