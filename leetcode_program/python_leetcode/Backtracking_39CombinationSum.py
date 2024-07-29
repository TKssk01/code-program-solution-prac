def combinationSum(candidates, target):
    # 結果を格納するリスト
    result = []

    # 再帰関数を定義。remaining_targetは残りのターゲット、startは開始インデックス、current_combinationは現在の組み合わせ
    def backtrack(remaining_target, start, current_combination):
        # 残りのターゲットが0になった場合、現在の組み合わせを結果リストに追加
        if remaining_target == 0:
            result.append(list(current_combination))
            return
        # 残りのターゲットが負になった場合、そのパスは無効なので戻る
        elif remaining_target < 0:
            return        
        # 候補リストをループし、再帰的に組み合わせを構築
        for i in range(start, len(candidates)):
            # 現在の数値を組み合わせに追加
            current_combination.append(candidates[i])
            # 残りのターゲットを更新し、再帰的に関数を呼び出し。同じインデックスを再度使用
            backtrack(remaining_target - candidates[i], i, current_combination)
            # 組み合わせから最後の要素を取り除く（バックトラック）
            current_combination.pop()
    # 再帰関数を初期値で呼び出す
    backtrack(target, 0, [])
    # 結果を返す
    return result

# テスト例
candidates1 = [2, 3, 6, 7]
target1 = 7
print(combinationSum(candidates1, target1))  # [[2, 2, 3], [7]]

candidates2 = [2, 3, 5]
target2 = 8
print(combinationSum(candidates2, target2))  # [[2, 2, 2, 2], [2, 3, 3], [3, 5]]

candidates3 = [2]
target3 = 1
print(combinationSum(candidates3, target3))  # []
