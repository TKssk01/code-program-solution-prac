import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)  # 利益のリストの長さを取得
        projects = list(zip(capital, profits))  # 資本と利益をペアにしてプロジェクトのリストを作成
        projects.sort()  # 初期資本の少ない順にプロジェクトをソート
        
        available_projects = []  # 現在の資本で実行可能なプロジェクト（最大ヒープ）
        i = 0  # 現在検討中のプロジェクトのインデックス
        
        for _ in range(k):  # 最大k回のプロジェクト選択
            while i < n and projects[i][0] <= w:
                # 現在の資本で実行可能なプロジェクトを最大ヒープに追加
                # マイナスを付けることで、最大ヒープとして機能させる
                heapq.heappush(available_projects, -projects[i][1])
                i += 1
            
            if not available_projects:
                # 実行可能なプロジェクトがない場合、ループを終了
                break
            
            # 最大の利益を持つプロジェクトを選択し、資本に加算
            w += -heapq.heappop(available_projects)
        
        return w  # 最終的な最大化された資本を返す

# テストケース
solution = Solution()
print(solution.findMaximizedCapital(k=2, w=0, profits=[1,2,3], capital=[0,1,1]))  # 出力: 4
print(solution.findMaximizedCapital(k=3, w=0, profits=[1,2,3], capital=[0,1,2]))  # 出力: 6
