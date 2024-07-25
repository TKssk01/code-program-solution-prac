# 必要なライブラリをインポート
from collections import defaultdict
# defaultdictは、存在しないキーにアクセスした際に
# 指定したデフォルト値（この場合は空のリスト）を自動的に生成する辞書型
from typing import List
# Solutionクラスを定義
class Solution:
    # コースを完了できるかどうかを判断するメソッドを定義
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # グラフを隣接リストとして表現するためのdefaultdictを作成
        graph = defaultdict(list)
        # prerequisitesリストをループして、グラフを構築
        for course, prereq in prerequisites:
            # 各コースの前提条件をグラフに追加
            graph[course].append(prereq)
        # 各コースの訪問状態を追跡するリストを初期化
        # 0: 未訪問, 1: 訪問中, 2: 訪問済み
        visited = [0] * numCourses
        # 深さ優先探索（DFS）を行う内部関数を定義
        def dfs(course):
            # 現在のコースが訪問中の場合、サイクルを検出したことになるのでFalseを返す
            if visited[course] == 1:
                return False
            # 現在のコースがすでに探索済みの場合、Trueを返す
            if visited[course] == 2:
                return True
            # 現在のコースを訪問中としてマーク
            visited[course] = 1
            # 現在のコースの依存関係（前提条件）を探索
            for prereq in graph[course]:
                # 依存関係のあるコースでDFSを再帰的に呼び出し、Falseが返されたら即座にFalseを返す
                if not dfs(prereq):
                    return False
            # すべての依存関係の探索が完了したら、現在のコースを訪問済みとしてマーク
            visited[course] = 2
            # サイクルが検出されなかったのでTrueを返す
            return True
        # すべてのコースに対してDFSを実行
        for course in range(numCourses):
            # いずれかのコースでサイクルが検出されたら即座にFalseを返す
            if not dfs(course):
                return False
        # すべてのコースでサイクルが検出されなかったのでTrueを返す
        return True