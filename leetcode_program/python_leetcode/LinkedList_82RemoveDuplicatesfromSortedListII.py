class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def deleteDuplicates(head: ListNode) -> ListNode:
    # ダミーノードを作成し、リストの先頭に追加
    dummy = ListNode(0)
    dummy.next = head
    # prevをダミーノードに設定
    prev = dummy
    # currentをリストの先頭に設定
    current = head
    while current:
        # 重複の検出
        if current.next and current.val == current.next.val:
            # 重複が続く間、次のノードに進む
            while current.next and current.val == current.next.val:
                current = current.next
            # 重複の削除: prev.next を current.next に設定
            prev.next = current.next
        else:
            # 重複がない場合、prevを進める
            prev = prev.next
        # currentを進める
        current = current.next
    # ダミーノードの次のノードを返す（新しいリストの先頭）
    return dummy.next
# 配列からリンクリストを作成するヘルパー関数
def create_linked_list(arr):
    if not arr:
        return None
    # リストの先頭を作成
    head = ListNode(arr[0])
    current = head
    # 残りの要素をリンクリストとして繋げる
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head
# リンクリストを配列に変換するヘルパー関数
def linked_list_to_array(head):
    array = []
    # リンクリストの各ノードの値を配列に追加
    while head:
        array.append(head.val)
        head = head.next
    return array

# テストケース 1
head = create_linked_list([1, 2, 3, 3, 4, 4, 5])
result = deleteDuplicates(head)
print(linked_list_to_array(result))  # [1, 2, 5]

# テストケース 2
head = create_linked_list([1, 1, 1, 2, 3])
result = deleteDuplicates(head)
print(linked_list_to_array(result))  # [2, 3]
