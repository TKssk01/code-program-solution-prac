from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list_new = ListNode()
        current = list_new

        while list1 and list2:
            if list1.val <= list2.val:
                current .next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return list_new.next
    
if __name__ == "__main__":
    # 与えられたリスト
    list1_elements = [1, 2, 4]
    list2_elements = [1, 3, 4]
    
    # 連結リストを作成
    list1 = ListNode(list1_elements)
    list2 = ListNode(list2_elements)
    
    # ソリューションのインスタンスを作成
    solution = Solution()
    
    # リストをマージ
    merged_list = solution.mergeTwoLists(list1, list2)
    
    # 結果を表示
    print(merged_list)