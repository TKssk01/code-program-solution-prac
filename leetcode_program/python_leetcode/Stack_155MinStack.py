class MinStack:
    def __init__(self):
        # 通常のスタックを保持するリスト
        self.stack = []
        # 最小値を保持するための補助スタック
        self.min_stack = []

    def push(self, val: int) -> None:
        # 値を通常のスタックに追加
        self.stack.append(val)
        # 補助スタックが空であるか、追加する値が補助スタックのトップの値以下であれば、補助スタックにも追加
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.stack:
            # 通常のスタックからトップの値を取り除く
            val = self.stack.pop()
            # 取り除いた値が補助スタックのトップの値と同じであれば、補助スタックからも取り除く
            if val == self.min_stack[-1]:
                self.min_stack.pop()

    def top(self) -> int:
        if self.stack:
            # 通常のスタックのトップの値を返す
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        if self.min_stack:
            # 補助スタックのトップの値（現在の最小値）を返す
            return self.min_stack[-1]
        return None