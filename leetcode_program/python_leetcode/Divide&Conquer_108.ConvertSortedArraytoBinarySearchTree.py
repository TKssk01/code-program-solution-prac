# 二分探索木のノードを定義するクラス
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # ノードの値を設定
        self.left = left  # 左の子ノードを設定
        self.right = right  # 右の子ノードを設定
# ソリューションクラス
class Solution:
    def sortedArrayToBST(self, nums):
        # 入力配列が空の場合はNoneを返す
        if not nums:
            return None
        # 中央のインデックスを計算する
        mid = len(nums) // 2
        # 中央要素をルートノードとする
        root = TreeNode(nums[mid])
        # 左右の部分配列で再帰的に部分木を構築する
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        # ルートノードを返す
        return root
# 助けとなる関数：結果の木を配列として出力するための関数
def treeToArray(root):
    # ルートノードがNoneの場合は空のリストを返す
    if not root:
        return []
    result = []  # 結果を格納するリスト
    queue = [root]  # ノードを探索するためのキュー

    while queue:
        node = queue.pop(0)  # キューの先頭ノードを取得
        if node:
            result.append(node.val)  # ノードの値を結果リストに追加
            queue.append(node.left)  # 左の子ノードをキューに追加
            queue.append(node.right)  # 右の子ノードをキューに追加
        else:
            result.append(None)  # ノードがNoneの場合、結果リストにNoneを追加
    
    # 最後のNoneは省略する
    while result and result[-1] is None:
        result.pop()    
    return result
# 例1のテスト
nums1 = [-10, -3, 0, 5, 9]
solution = Solution()  # Solutionクラスのインスタンスを作成
root1 = solution.sortedArrayToBST(nums1)  # 配列をBSTに変換
print(treeToArray(root1))  # 結果のBSTを配列形式で出力
# 例2のテスト
nums2 = [1, 3]
root2 = solution.sortedArrayToBST(nums2)  # 配列をBSTに変換
print(treeToArray(root2))  # 結果のBSTを配列形式で出力
