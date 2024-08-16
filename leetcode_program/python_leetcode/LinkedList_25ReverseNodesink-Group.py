class ListNode:
    def __init__(self, val=0, next=None):
        # ノードの値を初期化し、次のノードへのポインタを初期化
        self.val = val
        self.next = next
def reverseKGroup(head: ListNode, k: int) -> ListNode:
    # リストの長さを確認するための変数を初期化
    length = 0
    current = head
    # リストの長さを計算
    while current:
        length += 1
        current = current.next
    # ダミーノードを作成し、反転リストの先頭に接続
    dummy = ListNode(0)
    dummy.next = head
    # 前回の反転終了地点を保持するポインタ
    prev_end = dummy
    # リストがまだ反転可能なグループを含んでいる間繰り返す
    while length >= k:
        # 現在の反転する部分を追跡するためのポインタを初期化
        prev = None
        current = prev_end.next
        next = None
        # k個のノードを反転する
        for _ in range(k):
            # 次のノードを保持
            next = current.next
            # 現在のノードの次を前のノードに向ける（反転）
            current.next = prev
            # prevを更新して、現在のノードを指すようにする
            prev = current
            # currentを次のノードに進める
            current = next
        # 反転した部分の最後を次の部分とつなぐ
        tail = prev_end.next
        prev_end.next = prev
        tail.next = current
        # prev_endを反転した部分の最後に更新
        prev_end = tail
        # 残りの長さを減らす
        length -= k
    # 反転された新しいリストの先頭を返す
    return dummy.next