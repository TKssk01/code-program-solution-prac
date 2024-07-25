# 必要なライブラリをインポート
from collections import defaultdict, deque
# deque（デック）についての説明：
# dequeは「double-ended queue」の略で、両端キューと呼ばれるデータ構造です。
# 特徴：
# 1. リストと同様に要素の追加・削除ができますが、両端での操作が非常に効率的（O(1)の時間複雑度）です。
# 2. appendleft()とpopleft()メソッドにより、先頭への追加と削除が高速に行えます。
# 3. スレッドセーフであり、並行処理にも安全です。
# 4. メモリ効率が良く、要素数が増減してもメモリの再割り当てが最小限に抑えられます。
# 
# このプログラムでdequeを使用する理由：
# - トポロジカルソートのアルゴリズムでは、処理すべき頂点（講義）のキューが必要です。
# - dequeを使うことで、キューの先頭からの要素の取り出し（popleft）が効率的に行えます。
# - もし通常のリストを使用した場合、先頭からの要素の削除（pop(0)）はO(n)の時間がかかりますが、
#   dequeではO(1)で行えるため、特に要素数が多い場合に効率的です。

# 講義の順序を見つける関数を定義
def findOrder(numCourses, prerequisites):
    # グラフを表現するためのデフォルト辞書を初期化（キーが存在しない場合、空のリストを返す）
    graph = defaultdict(list)
    # 各講義の入次数（依存している講義の数）を記録するリストを初期化
    in_degree = [0] * numCourses
    
    # 前提条件のリストをループして、グラフを構築し入次数を計算
    for course, prereq in prerequisites:
        # prereqからcourseへのエッジをグラフに追加
        graph[prereq].append(course)
        # courseの入次数を1増やす
        in_degree[course] += 1
    
    # 入次数が0の講義（前提条件のない講義）をキューに追加
    queue = deque([course for course in range(numCourses) if in_degree[course] == 0])
    # 結果を格納するリストを初期化
    result = []
    
    # キューが空になるまでループ（トポロジカルソートの主要部分）
    while queue:
        # キューから講義を取り出す
        current = queue.popleft()
        # 取り出した講義を結果リストに追加
        result.append(current)
        
        # 取り出した講義に依存している講義をループ
        for neighbor in graph[current]:
            # 依存している講義の入次数を1減らす
            in_degree[neighbor] -= 1
            # もし入次数が0になったら、その講義をキューに追加
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # 全ての講義を訪問できた場合は結果リストを返し、そうでない場合は空リストを返す
    return result if len(result) == numCourses else []

# 使用例：4つの講義と4つの前提条件がある場合
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# findOrder関数を呼び出し、結果を表示
print(findOrder(numCourses, prerequisites))