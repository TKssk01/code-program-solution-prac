def letterCombinations(digits: str):
    # 数字から文字へのマッピングを定義
    digit_to_char = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    
    # 入力が空の場合は空のリストを返す
    if not digits:
        return []
    
    # 再帰的に組み合わせを生成する関数を定義
    def backtrack(index, path):
        # すべての数字を処理し終えた場合の基底ケース
        if index == len(digits):
            # 現在のパスを文字列に変換して結果リストに追加
            combinations.append(''.join(path))
            return
        
        # 現在の数字に対応するすべての文字を取得
        possible_chars = digit_to_char[digits[index]]
        
        # 各文字について再帰呼び出しを行う
        for char in possible_chars:
            # 現在の文字をパスに追加
            path.append(char)
            # 次の数字に対して再帰呼び出し
            backtrack(index + 1, path)
            # 再帰呼び出し後にパスから現在の文字を取り除く
            path.pop()
    
    # 結果を格納するリストを初期化
    combinations = []
    # 再帰関数を初期インデックスと空のパスで呼び出す
    backtrack(0, [])
    
    # すべての組み合わせを返す
    return combinations

# 例のテストケースを実行
print(letterCombinations("23"))  # 出力: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letterCombinations(""))    # 出力: []
print(letterCombinations("2"))   # 出力: ["a","b","c"]
