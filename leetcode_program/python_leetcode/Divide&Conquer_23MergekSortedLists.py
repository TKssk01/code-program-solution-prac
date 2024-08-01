class ListNode:
    # リンクリストのノードを定義
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    # 2つのソート済みリンクリストをマージするヘルパー関数を定義
    def mergeTwoLists(l1, l2):
        # ダミーノードを作成し、現在のノードを指すポインタを初期化
        dummy = ListNode()
        current = dummy
        # 2つのリストが共に存在する間ループ
        while l1 and l2:
            # l1の値がl2の値より小さい場合、l1のノードを現在のノードにリンク
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            # l2の値がl1の値より小さい場合、l2のノードを現在のノードにリンク
            else:
                current.next = l2
                l2 = l2.next
            # 現在のノードを進める
            current = current.next
        # 残っているリストのノードをリンク
        current.next = l1 if l1 else l2
        return dummy.next
    # リストが空の場合、Noneを返す
    if not lists:
        return None
    # リストが1つだけの場合、そのリストを返す
    if len(lists) == 1:
        return lists[0]
    # リストを半分に分ける
    mid = len(lists) // 2
    # 左半分を再帰的にマージ
    left = mergeKLists(lists[:mid])
    # 右半分を再帰的にマージ
    right = mergeKLists(lists[mid:])
    
    # 2つのマージされたリストをマージ
    return mergeTwoLists(left, right)

# 配列からリンクリストを作成するためのヘルパー関数
def create_linked_list(arr):
    # 配列が空の場合、Noneを返す
    if not arr:
        return None
    # リンクリストのヘッドを作成
    head = ListNode(arr[0])
    current = head
    # 配列の各要素をリンクリストのノードとして追加
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# リンクリストを配列に変換するためのヘルパー関数
def linked_list_to_array(node):
    array = []
    # リンクリストの各ノードの値を配列に追加
    while node:
        array.append(node.val)
        node = node.next
    return array

# 入力をリンクリストとして作成
lists = [[1,4,5],[1,3,4],[2,6]]
linked_lists = [create_linked_list(l) for l in lists]

# マージして結果を配列に変換
merged_head = mergeKLists(linked_lists)
result = linked_list_to_array(merged_head)

# 結果の表示
print(result)  # 出力: [1, 1, 2, 3, 4, 4, 5, 6]
