from typing import List

# ノードクラスの定義
class Node:
    # コンストラクタ: ノードの初期化
    def __init__(self, val = 0, neighbors = None):
        # ノードの値を設定
        self.val = val
        # 隣接ノードのリストを設定（デフォルトは空リスト）
        self.neighbors = neighbors if neighbors is not None else []
# グラフのクローンを作成するためのSolutionクラス
class Solution:
    # グラフをクローンするメソッド
    def cloneGraph(self, node: 'Node') -> 'Node':
        # 入力が空の場合、Noneを返す
        if not node:
            return None
        # 元のノードと新しいノードの対応を記録するための辞書
        old_to_new = {}
        # 深さ優先探索（DFS）を行う内部関数
        def dfs(node):
            # ノードが既にコピー済みの場合、そのコピーを返す
            if node in old_to_new:
                return old_to_new[node]
            # 新しいノードを作成
            copy = Node(node.val)
            # 辞書に新しいノードを記録
            old_to_new[node] = copy
            # 隣接ノードを再帰的にコピー
            for neighbor in node.neighbors:
                # コピーしたノードの隣接リストに追加
                copy.neighbors.append(dfs(neighbor))
            # コピーしたノードを返す
            return copy
        # DFSを開始し、クローンしたグラフを返す
        return dfs(node)
# 隣接リストからグラフを構築する関数
def build_graph(adj_list):
    # 隣接リストが空の場合、Noneを返す
    if not adj_list:
        return None
    # 各ノードを作成
    nodes = [Node(i+1) for i in range(len(adj_list))]
    # 各ノードの隣接ノードを設定
    for i, neighbors in enumerate(adj_list):
        nodes[i].neighbors = [nodes[j-1] for j in neighbors]
    # 最初のノードを返す
    return nodes[0]
# テストケース1: 4ノードの連結グラフ
adj_list1 = [[2,4],[1,3],[2,4],[1,3]]
# グラフを構築
original1 = build_graph(adj_list1)
# Solutionクラスのインスタンスを作成
solution = Solution()
# グラフをクローン
cloned1 = solution.cloneGraph(original1)

# テストケース2: 1ノードのグラフ
adj_list2 = [[]]
# グラフを構築
original2 = build_graph(adj_list2)
# グラフをクローン
cloned2 = solution.cloneGraph(original2)

# テストケース3: 空のグラフ
adj_list3 = []
# グラフを構築
original3 = build_graph(adj_list3)
# グラフをクローン
cloned3 = solution.cloneGraph(original3)

# テストケースが正常に実行されたことを出力
print("Test cases executed successfully")