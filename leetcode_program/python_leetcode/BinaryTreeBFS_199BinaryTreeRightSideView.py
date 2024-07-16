from collections import deque  # dequeをインポート（キューとして使用）

# 二分木のノードを表すクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        # ノードの値を初期化
        self.val = val
        # 左の子ノードを初期化
        self.left = left
        # 右の子ノードを初期化
        self.right = right

# 右側から見たときに見えるノードの値を返す関数
def rightSideView(root):
    # もし根ノードが存在しない場合、空のリストを返す
    if not root:
        return []

    # キューを初期化し、根ノードを追加
    queue = deque([root])
    # 結果を格納するリストを初期化
    right_view = []

    # キューが空になるまでループ
    while queue:
        # 現在のレベルのノード数を取得
        level_length = len(queue)
        # 現在のレベルのノードをすべて探索
        for i in range(level_length):
            # キューからノードを取り出す
            node = queue.popleft()
            # このレベルの最後のノードの場合
            if i == level_length - 1:
                # 結果リストにノードの値を追加
                right_view.append(node.val)
            # 左の子ノードが存在する場合
            if node.left:
                # 左の子ノードをキューに追加
                queue.append(node.left)
            # 右の子ノードが存在する場合
            if node.right:
                # 右の子ノードをキューに追加
                queue.append(node.right)

    # 右側から見たときに見えるノードの値のリストを返す
    return right_view

# テスト例
root1 = TreeNode(1)  # 根ノードを作成
root1.left = TreeNode(2)  # 左の子ノードを追加
root1.right = TreeNode(3)  # 右の子ノードを追加
root1.left.left = TreeNode(4)  # 左の子ノードの左の子ノードを追加

# 出力: [1, 3, 4]
print(rightSideView(root1))
