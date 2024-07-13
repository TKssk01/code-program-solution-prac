class Solution:
    def simplifyPath(self, path: str) -> str:
        # パスをスラッシュで分割し、各部分をリストに格納
        parts = path.split('/')
        # スタックを初期化
        stack = []
        # 各部分を順に処理
        for part in parts:
            # 空文字列または「.」は無視
            if part == '' or part == '.':
                continue
            # 「..」の場合、スタックが空でなければ一番上をポップ
            elif part == '..':
                if stack:
                    stack.pop()
            # それ以外の場合、スタックにプッシュ
            else:
                stack.append(part)
        # スタックの内容をスラッシュで連結し、先頭にスラッシュを付けて正規化されたパスを構築
        canonical_path = '/' + '/'.join(stack)
        return canonical_path

# テストケース
test_cases = [
    "/home/",
    "/home//foo/",
    "/home/user/Documents/../Pictures",
    "/../",
    "/.../a/../b/c/../d/./"
]

# Solutionクラスのインスタンスを作成
solution = Solution()

# 各テストケースの結果を表示
for path in test_cases:
    print(f"Input: {path}")
    print(f"Output: {solution.simplifyPath(path)}")
    print()