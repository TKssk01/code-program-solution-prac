class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # ノードの値を初期化
        self.next = next  # 次のノードへのポインタを初期化

def rotateRight(head, k):
    # リストが空、要素が1つしかない、またはkが0の場合はそのまま返す
    if not head or not head.next or k == 0:
        return head

    # リストの長さを計算
    length = 1
    current = head
    while current.next:
        current = current.next
        length += 1

    # kの正規化（kがリストの長さ以上の場合を考慮）
    k = k % length
    if k == 0:
        return head

    # 新しい先頭と末尾を決定
    new_tail_position = length - k  # 新しい末尾の位置
    new_tail = head
    for _ in range(new_tail_position - 1):
        new_tail = new_tail.next
    
    new_head = new_tail.next  # 新しい先頭
    new_tail.next = None  # 新しい末尾の次をNoneに設定

    # 元の末尾を新しいリストの先頭にリンク
    current.next = head

    return new_head

# リストを作成するヘルパー関数
def create_linked_list(elements):
    # リストが空の場合
    if not elements:
        return None
    head = ListNode(elements[0])  # リストの先頭を初期化
    current = head
    for val in elements[1:]:
        current.next = ListNode(val)  # 新しいノードを追加
        current = current.next  # currentを次に進める
    return head

# リストを表示するヘルパー関数
def print_linked_list(head):
    current = head
    elements = []
    while current:
        elements.append(current.val)  # ノードの値をリストに追加
        current = current.next  # currentを次に進める
    print(elements)

# テスト
head = create_linked_list([1, 2, 3, 4, 5])  # リストを作成
k = 2  # 回転する回数
rotated_head = rotateRight(head, k)  # リストを回転
print_linked_list(rotated_head)  # 回転後のリストを表示

head = create_linked_list([0, 1, 2])  # 別のリストを作成
k = 4  # 回転する回数
rotated_head = rotateRight(head, k)  # リストを回転
print_linked_list(rotated_head)  # 回転後のリストを表示
