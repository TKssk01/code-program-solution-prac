from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: ListNode, n: int) -> ListNode:
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    # Move fast ahead by n steps
    for _ in range(n):
        fast = fast.next
    
    # Move both fast and slow until fast reaches the end
    while fast.next:
        fast = fast.next
        slow = slow.next
    
    # Remove the nth node from the end
    slow.next = slow.next.next
    
    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    vals = []
    current = head
    while current:
        vals.append(current.val)
        current = current.next
    return vals

# Test cases
head1 = create_linked_list([1,2,3,4,5])
n1 = 2
result1 = removeNthFromEnd(head1, n1)
print(print_linked_list(result1))  # [1, 2, 3, 5]

head2 = create_linked_list([1])
n2 = 1
result2 = removeNthFromEnd(head2, n2)
print(print_linked_list(result2))  # []

head3 = create_linked_list([1, 2])
n3 = 1
result3 = removeNthFromEnd(head3, n3)
print(print_linked_list(result3))  # [1]
