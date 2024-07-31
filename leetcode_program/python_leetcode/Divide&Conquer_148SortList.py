from typing import Optional
# ListNodeクラスの定義
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solutionクラスの定義
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # リストが空または要素が一つの場合、リストをそのまま返す
        if not head or not head.next:
            return head

        # リストを二つに分割するための関数
        def split(head):
            # スローランナーとファストランナーを初期化
            slow, fast = head, head.next
            # ファストランナーがリストの終端に到達するまでループ
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            # リストを二つに分割
            mid = slow.next
            slow.next = None
            return head, mid
        # 二つのソートされたリストをマージするための関数
        def merge(l1, l2):
            # ダミーノードを作成
            dummy = ListNode()
            tail = dummy
            # 両方のリストが空でない間ループ
            while l1 and l2:
                if l1.val < l2.val:
                    # l1の現在のノードが小さい場合、tailに追加
                    tail.next = l1
                    l1 = l1.next
                else:
                    # l2の現在のノードが小さい場合、tailに追加
                    tail.next = l2
                    l2 = l2.next
                # tailを次の位置に移動
                tail = tail.next
            # 残ったノードを追加
            if l1:
                tail.next = l1
            else:
                tail.next = l2
            return dummy.next
        # リストを二つに分割
        left, right = split(head)
        # 左側のリストを再帰的にソート
        left = self.sortList(left)
        # 右側のリストを再帰的にソート
        right = self.sortList(right)
        # ソートされたリストをマージして返す
        return merge(left, right)
# リストの構築
node1 = ListNode(4)
node2 = ListNode(2)
node3 = ListNode(1)
node4 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node4
# Solutionオブジェクトを作成
solution = Solution()
# リストをソート
sorted_head = solution.sortList(node1)
# ソートされたリストの出力
current = sorted_head
while current:
    # 現在のノードの値を出力
    print(current.val, end=" ")
    # 次のノードに移動
    current = current.next
