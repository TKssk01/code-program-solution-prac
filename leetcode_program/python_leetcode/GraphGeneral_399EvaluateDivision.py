# 必要なモジュールをインポート
from collections import defaultdict
from typing import List
# Solutionクラスを定義
class Solution:
    # メインメソッドの定義。方程式、値、クエリを引数として受け取り、結果のリストを返す
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # グラフの構築。defaultdictを使用して、存在しないキーに対してもエラーを発生させずに辞書を返す
        graph = defaultdict(dict)
        # 方程式と値のペアをイテレート
        for (x, y), value in zip(equations, values):
            # グラフに順方向のエッジを追加
            graph[x][y] = value
            # グラフに逆方向のエッジを追加（値の逆数）
            graph[y][x] = 1 / value
        # 深さ優先探索（DFS）関数の定義
        def dfs(x: str, y: str, visited: set) -> float:
            # xまたはyがグラフに存在しない場合、-1.0を返す
            if x not in graph or y not in graph:
                return -1.0
            # xとyが同じ場合、1.0を返す
            if x == y:
                return 1.0
            # 現在のノードを訪問済みとしてマーク
            visited.add(x)
            # 現在のノードの隣接ノードをイテレート
            for neighbor in graph[x]:
                # 隣接ノードが未訪問の場合
                if neighbor not in visited:
                    # 隣接ノードから目的地までのDFSを再帰的に呼び出し
                    result = dfs(neighbor, y, visited)
                    # 有効な結果が得られた場合
                    if result != -1.0:
                        # 現在のエッジの重みと再帰呼び出しの結果を掛けて返す
                        return result * graph[x][neighbor]
            # バックトラッキング：訪問済みセットから現在のノードを削除
            visited.remove(x)
            # パスが見つからなかった場合、-1.0を返す
            return -1.0
        # クエリの処理
        results = []
        # 各クエリに対してDFSを実行
        for query in queries:
            result = dfs(query[0], query[1], set())
            # 結果をリストに追加
            results.append(result)
        # 全クエリの結果を返す
        return results
# テストケースの定義
equations = [["a","b"],["b","c"]]
values = [2.0,3.0]
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Solutionクラスのインスタンスを作成
solution = Solution()
# calcEquationメソッドを呼び出し、結果を出力
print(solution.calcEquation(equations, values, queries))