from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # グリッドが空でないか確認
        if not grid:
            return 0
        def dfs(grid, start_i, start_j):
            # スタックを初期化し、最初のセルを追加
            stack = [(start_i, start_j)]
            while stack:
                # スタックから現在のセルを取得
                i, j = stack.pop()
                # セルがグリッドの境界外または既に訪問済みかどうかをチェック
                if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] == '0':
                    continue
                # 現在のセルを訪問済みとしてマーク
                grid[i][j] = '0'
                # 下のセルをスタックに追加
                stack.append((i+1, j))
                # 上のセルをスタックに追加
                stack.append((i-1, j))
                # 右のセルをスタックに追加
                stack.append((i, j+1))
                # 左のセルをスタックに追加
                stack.append((i, j-1))
        # 島のカウントを初期化
        count = 0
        # グリッドの各セルをスキャン
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # '1' を見つけたら新しい島としてDFSを開始
                if grid[i][j] == '1':
                    dfs(grid, i, j)
                    count += 1  # 島のカウントを増やす
        return count
# テストケース
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
sol = Solution()
print(f'Number of islands: {sol.numIslands(grid)}')
