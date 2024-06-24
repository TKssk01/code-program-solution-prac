from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # 両方ともNoneの場合、同じとみなす
        if not p and not q:
            return True
        # どちらか片方がNoneの場合、異なるとみなす
        if not p or not q:
            return False
        # 現在のノードの値が異なる場合、異なるとみなす
        if p.val != q.val:
            return False
        # 左の子ノードと右の子ノードを再帰的にチェック
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

def run_tests():

    sol = Solution()
    # テストケース1: 同じ木
    p1 = TreeNode(1, TreeNode(2), TreeNode(3))
    q1 = TreeNode(1, TreeNode(2), TreeNode(3))
    assert sol.isSameTree(p1, q1) == True, "Test Case 1 Failed"

    # テストケース2: 異なる木（構造が異なる）
    p2 = TreeNode(1, TreeNode(2))
    q2 = TreeNode(1, None, TreeNode(2))
    assert sol.isSameTree(p2, q2) == False, "Test Case 2 Failed"

    # テストケース3: 異なる木（値が異なる）
    p3 = TreeNode(1, TreeNode(2), TreeNode(3))
    q3 = TreeNode(1, TreeNode(2), TreeNode(4))
    assert sol.isSameTree(p3, q3) == False, "Test Case 3 Failed"

    # テストケース4: 片方の木が空
    p4 = TreeNode(1, TreeNode(2), TreeNode(3))
    q4 = None
    assert sol.isSameTree(p4, q4) == False, "Test Case 4 Failed"

    # テストケース5: 両方の木が空
    p5 = None
    q5 = None
    assert sol.isSameTree(p5, q5) == True, "Test Case 5 Failed"

    # テストケース6: 部分的に同じだが完全には同じでない木
    p6 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4))
    q6 = TreeNode(1, TreeNode(2), TreeNode(4))
    assert sol.isSameTree(p6, q6) == False, "Test Case 6 Failed"

    print("All test cases passed!")

# テストを実行
run_tests()

    