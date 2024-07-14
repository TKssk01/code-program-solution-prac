import random

class RandomizedSet:

    def __init__(self):
        # 値からそのインデックスへのマッピングを保持する辞書
        self.val_to_index = {}
        # セットの全ての値を保持するリスト
        self.values = []

    def insert(self, val: int) -> bool:
        # 値が既にセットに存在するかをチェック
        if val in self.val_to_index:
            return False
        # 値をリストの末尾に追加
        self.values.append(val)
        # 辞書に値とそのインデックスを追加
        self.val_to_index[val] = len(self.values) - 1
        return True

    def remove(self, val: int) -> bool:
        # 値がセットに存在しない場合はFalseを返す
        if val not in self.val_to_index:
            return False
        # 削除する値のインデックスを取得
        index = self.val_to_index[val]
        # リストの末尾の値を取得
        last_val = self.values[-1]
        # 削除する値の位置に末尾の値を移動
        self.values[index] = last_val
        # 末尾の値のインデックスを更新
        self.val_to_index[last_val] = index
        # リストの末尾の値を削除
        self.values.pop()
        # 辞書から削除する値のエントリを削除
        del self.val_to_index[val]
        return True

    def getRandom(self) -> int:
        # リストからランダムな要素を返す
        return random.choice(self.values)
    
# 操作シーケンスと引数
operations = ["RandomizedSet", "insert", "remove", "insert", "getRandom", "remove", "insert", "getRandom"]
arguments = [[], [1], [2], [2], [], [1], [2], []]

# 結果を保持するリスト
results = []

# シードを設定してランダム性を固定
# random.seed(0)

# RandomizedSetクラスのインスタンスを初期化
obj = None

# 各操作を順番に実行
for i, operation in enumerate(operations):
    if operation == "RandomizedSet":
        obj = RandomizedSet()
        results.append(None)  # 初期化の結果はnull（PythonではNone）
    elif operation == "insert":
        result = obj.insert(arguments[i][0])
        results.append(result)
    elif operation == "remove":
        result = obj.remove(arguments[i][0])
        results.append(result)
    elif operation == "getRandom":
        result = obj.getRandom()
        results.append(result)

# 結果を表示
print(results)

# 使用例
# obj = RandomizedSet()
# param_1 = obj.insert(1)
# param_2 = obj.remove(2)
# param_3 = obj.insert(2)
# param_4 = obj.getRandom()
# param_5 = obj.remove(1)
# param_6 = obj.insert(2)
# param_7 = obj.getRandom()
