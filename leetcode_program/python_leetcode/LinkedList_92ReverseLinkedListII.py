class ListNode:
    def __init__(self, val=0, next=None):
        # ノードの値を初期化
        self.val = val
        # 次のノードへのポインタを初期化
        self.next = next
def reverseBetween(head: ListNode, left: int, right: int) -> ListNode:
    # リストが空の場合やleftとrightが同じ場合はそのまま返す
    if not head or left == right:
        return head
    # ダミーヘッドを作成
    dummy = ListNode(0)
    # ダミーヘッドの次を元のリストのヘッドに設定
    dummy.next = head
    # prevをダミーヘッドに設定
    prev = dummy
    # ステップ1: `prev` を `left` の前のノードに移動
    for _ in range(left - 1):
        # `prev` を `left` の前のノードに移動
        prev = prev.next
    # ステップ2: `left` から `right` までのサブリストを逆順にする
    # currentを`left` のノードに設定
    current = prev.next
    # next_nodeの初期化
    next_node = None
    for _ in range(right - left):
        # 次のノードを取得
        next_node = current.next
        # currentの次を次の次に設定
        current.next = next_node.next
        # next_nodeを逆順の先頭に設定
        next_node.next = prev.next
        # prevの次をnext_nodeに設定
        prev.next = next_node
    # ダミーヘッドの次のノードを返す（新しいリストのヘッド）
    return dummy.next
# 使用例:
# 入力: head = [1,2,3,4,5], left = 2, right = 4
# 期待される出力: [1,4,3,2,5]
def print_list(head: ListNode):
    while head:
        # ノードの値を出力
        print(head.val, end=" -> ")
        # 次のノードに移動
        head = head.next
    # リストの終わりを表示
    print("None")
# リスト [1,2,3,4,5] の作成
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
# 関数の適用
new_head = reverseBetween(head, 2, 4)
# 結果の表示
print_list(new_head)  # 新しいリストの表示
