class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値を初期化
        self.next = next  # 次のノードへのポインタを初期化

def partition(head: ListNode, x: int) -> ListNode:
    # xより小さいノードを格納するダミーヘッド
    small_head = ListNode(0)
    small = small_head  # smallリストの現在位置を示すポインタ

    # x以上のノードを格納するダミーヘッド
    large_head = ListNode(0)
    large = large_head  # largeリストの現在位置を示すポインタ

    # リストを順に走査
    current = head
    while current:
        if current.val < x:  # ノードの値がxより小さい場合
            small.next = current  # smallリストにノードを追加
            small = small.next  # smallポインタを更新
        else:  # ノードの値がx以上の場合
            large.next = current  # largeリストにノードを追加
            large = large.next  # largeポインタを更新
        current = current.next  # 次のノードへ移動

    # largeリストの終わりを示す
    large.next = None
    # smallリストの終わりをlargeリストの始まりに繋ぐ
    small.next = large_head.next

    return small_head.next  # 新しいリストの先頭を返す
