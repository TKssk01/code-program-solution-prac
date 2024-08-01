# ノードクラスの定義
class Node:
    # ノードを初期化するコンストラクタ
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val  # ノードの値 (True or False)
        self.isLeaf = isLeaf  # ノードがリーフノードかどうかのフラグ
        self.topLeft = topLeft  # トップ左の子ノード
        self.topRight = topRight  # トップ右の子ノード
        self.bottomLeft = bottomLeft  # ボトム左の子ノード
        self.bottomRight = bottomRight  # ボトム右の子ノード

# グリッドからクワッドツリーを構築する関数
def construct(grid):
    # サブグリッドが同じ値か確認する関数
    def is_unified(grid, row_start, row_end, col_start, col_end):
        initial = grid[row_start][col_start]  # サブグリッドの初期値を取得
        # サブグリッドの各セルが初期値と同じか確認
        for r in range(row_start, row_end):
            for c in range(col_start, col_end):
                if grid[r][c] != initial:
                    return False, None  # 異なる値があればFalseを返す
        return True, initial  # 全て同じ値であればTrueとその値を返す
    # 再帰的にクワッドツリーを構築する関数
    def construct_quad(row_start, row_end, col_start, col_end):
        # サブグリッドが同じ値か確認
        unified, value = is_unified(grid, row_start, row_end, col_start, col_end)
        if unified:
            return Node(value == 1, True)  # リーフノードとしてノードを作成
        # サブグリッドの中間点を計算
        row_mid = (row_start + row_end) // 2
        col_mid = (col_start + col_end) // 2
        # 4つのサブグリッドに分割し、それぞれ再帰的にクワッドツリーを構築
        topLeft = construct_quad(row_start, row_mid, col_start, col_mid)
        topRight = construct_quad(row_start, row_mid, col_mid, col_end)
        bottomLeft = construct_quad(row_mid, row_end, col_start, col_mid)
        bottomRight = construct_quad(row_mid, row_end, col_mid, col_end)
        # 内部ノードとしてノードを作成
        return Node(True, False, topLeft, topRight, bottomLeft, bottomRight)
    # グリッド全体に対してクワッドツリーの構築を開始
    return construct_quad(0, len(grid), 0, len(grid[0]))
# テスト用のグリッド
grid = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]
# クワッドツリーを構築
quad_tree = construct(grid)
