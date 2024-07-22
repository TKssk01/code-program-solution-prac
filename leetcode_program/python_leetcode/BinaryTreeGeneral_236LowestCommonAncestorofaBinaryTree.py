from typing import Optional

# 二分木のノードを表すクラス定義
class TreeNode:
    # コンストラクタ：ノードの値を初期化し、左右の子ノードをNoneに設定
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# LCAを見つけるためのSolutionクラス
class Solution:
    # LCAを見つけるメソッド。引数は根ノードと2つのターゲットノード
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # ベースケース：ルートがNoneか、pまたはqと一致する場合
        if root is None or root == p or root == q:
            return root
        # 左の子ノードを再帰的に探索
        left = self.lowestCommonAncestor(root.left, p, q)
        # 右の子ノードを再帰的に探索
        right = self.lowestCommonAncestor(root.right, p, q)
        # 左右の子ノードの結果に基づいてLCAを決定
        if left and right:
            # pとqが異なる部分木で見つかった場合、現在のノードがLCA
            return root
        elif left:
            # pまたはqが左部分木で見つかった場合
            return left
        elif right:
            # pまたはqが右部分木で見つかった場合
            return right
        else:
            # pもqも見つからなかった場合
            return None
# テスト用のヘルパー関数：配列から二分木を構築
def build_tree(values):
    # 空の配列の場合、Noneを返す
    if not values:
        return None
    # 根ノードを作成
    root = TreeNode(values[0])
    # 幅優先探索のためのキューを初期化
    queue = [root]
    i = 1
    # キューが空になるか、すべての値が処理されるまでループ
    while queue and i < len(values):
        # キューから次のノードを取り出す
        node = queue.pop(0)
        # 左の子ノードを作成（存在する場合）
        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1
        # 右の子ノードを作成（存在する場合）
        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1
    # 構築された木の根ノードを返す
    return root
# メイン処理：テストケースの実行
if __name__ == "__main__":
    # テストケース1：[3,5,1,6,2,0,8,None,None,7,4]の木を構築
    root1 = build_tree([3,5,1,6,2,0,8,None,None,7,4])
    # Solutionクラスのインスタンスを作成
    solution = Solution()
    # ノード5（root1.left）とノード1（root1.right）のLCAを求める
    p1, q1 = root1.left, root1.right
    result1 = solution.lowestCommonAncestor(root1, p1, q1)
    # 結果を出力（期待される出力: 3）
    print(f"Test Case 1 Result: {result1.val}")
    # テストケース2：同じ木でノード5とノード4のLCAを求める
    p2, q2 = root1.left, root1.left.right.right
    result2 = solution.lowestCommonAncestor(root1, p2, q2)
    # 結果を出力（期待される出力: 5）
    print(f"Test Case 2 Result: {result2.val}")
    # テストケース3：[1,2]の木を構築
    root2 = build_tree([1,2])
    # ノード1（root2）とノード2（root2.left）のLCAを求める
    p3, q3 = root2, root2.left
    result3 = solution.lowestCommonAncestor(root2, p3, q3)
    # 結果を出力（期待される出力: 1）
    print(f"Test Case 3 Result: {result3.val}")