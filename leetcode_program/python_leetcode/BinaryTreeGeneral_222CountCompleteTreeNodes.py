from typing import Optional
# 二分木のノードを表すクラスを定義
class TreeNode:
    # コンストラクタ：ノードの値と左右の子ノードを初期化
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値
        self.left = left  # 左の子ノード
        self.right = right  # 右の子ノード

class Solution:
    # 完全二分木のノード数を数えるメソッド
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # ルートノードが存在しない場合、0を返す
        if not root:
            return 0

        # 木の深さ（高さ）を取得する内部関数
        def get_depth(node):
            depth = 0
            # 左端のノードまで進みながら深さを数える
            while node.left:
                node = node.left
                depth += 1
            return depth

        # 指定されたインデックスのノードが存在するかを確認する内部関数
        def exists(idx, depth, node):
            # 二分探索の範囲を初期化
            left, right = 0, 2**depth - 1

            # 深さの分だけ繰り返し
            for _ in range(depth):
                # 中間点を計算
                mid = left + (right - left) // 2
                # インデックスが中間点以下なら左に、そうでなければ右に進む
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            # ノードが存在すればTrue、そうでなければFalseを返す
            return node is not None
        
        # 木の深さを取得
        depth = get_depth(root)

        # 深さが0（ルートノードのみ）の場合、1を返す
        if depth == 0:
            return 1
        
        # 最後の層のノード数を二分探索で求める
        left, right = 1, 2**depth - 1
        while left <= right:
            # 中間点を計算
            mid = left + (right - left) // 2
            # 中間点のノードが存在する場合、左側の探索範囲を狭める
            if exists(mid, depth, root):
                left = mid + 1
            # 存在しない場合、右側の探索範囲を狭める
            else:
                right = mid - 1

        # 完全に埋まった層のノード数 + 最後の層のノード数を返す
        return (2**depth - 1) + left