from typing import Optional

class Node:
    def __init__(self, val=0, next=None, random=None):
        # ノードの初期化
        self.val = val
        self.next = next
        self.random = random
def copyRandomList(head):
    if not head:
        # リストが空の場合、Noneを返す
        return None
    # 1. ノードの複製とインターリーブ
    current = head
    while current:
        # 現在のノードの複製を作成
        new_node = Node(current.val)
        # 複製ノードのnextを現在のノードのnextに設定
        new_node.next = current.next
        # 現在のノードのnextを複製ノードに設定
        current.next = new_node
        # 次のオリジナルのノードに進む
        current = new_node.next
    # 2. ランダムポインタの設定
    current = head
    while current:
        if current.random:
            # 複製ノードのrandomを現在のノードのrandomの次のノードに設定
            current.next.random = current.random.next
        # 次のオリジナルのノードに進む
        current = current.next.next
    # 3. リストの分離
    current = head
    # 新しいリストのヘッドを保存
    new_head = head.next
    while current:
        # 複製ノードを取得
        new_node = current.next
        # オリジナルのノードのnextを修正
        current.next = new_node.next
        if new_node.next:
            # 複製ノードのnextを修正
            new_node.next = new_node.next.next
        # 次のオリジナルのノードに進む
        current = current.next
    # 複製されたリストのヘッドを返す
    return new_head

def build_list(values):
    if not values:
        return None
    nodes = [Node(val) for val, _ in values]
    head = nodes[0]
    for i, (val, rand_idx) in enumerate(values):
        if i < len(nodes) - 1:
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]
    return head

def print_list(head):
    result = []
    while head:
        rand_val = head.random.val if head.random else None
        result.append([head.val, rand_val])
        head = head.next
    print(result)

# リストの例
values = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
head = build_list(values)

print("元のリスト:")
print_list(head)

copied_head = copyRandomList(head)

print("ディープコピーされたリスト:")
print_list(copied_head)