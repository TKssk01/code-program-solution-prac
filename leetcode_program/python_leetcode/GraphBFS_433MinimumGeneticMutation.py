from collections import deque

def minMutation(startGene, endGene, bank):
    # バンクをセットに変換して効率的に検索できるようにする
    bank_set = set(bank)
    # エンド遺伝子がバンクにない場合、変異は不可能
    if endGene not in bank_set:
        return -1
    # キューに初期状態としてスタート遺伝子とステップ数0を追加
    queue = deque([(startGene, 0)])
    # 訪問済みセットにスタート遺伝子を追加
    visited = set([startGene])
    # BFSループ
    while queue:
        # キューから現在の遺伝子とステップ数を取得
        current_gene, steps = queue.popleft()
        # エンド遺伝子に到達した場合、現在のステップ数を返す
        if current_gene == endGene:
            return steps
        # 現在の遺伝子の各位置についてループ
        for i in range(len(current_gene)):
            # 'A', 'C', 'G', 'T' の各文字についてループ
            for char in 'ACGT':
                # 同じ文字に変異しないようにするためのチェック
                if char != current_gene[i]:
                    # 一文字変異させた次の遺伝子を生成
                    next_gene = current_gene[:i] + char + current_gene[i+1:]
                    # 有効な遺伝子であり、かつまだ訪問していない場合
                    if next_gene in bank_set and next_gene not in visited:
                        # 訪問済みとしてマーク
                        visited.add(next_gene)
                        # キューに次の遺伝子とステップ数+1を追加
                        queue.append((next_gene, steps + 1))
    # エンド遺伝子に到達できない場合、-1を返す
    return -1

# 実行例
# スタート遺伝子 "AACCGGTT" からエンド遺伝子 "AACCGGTA" への変異は1ステップで可能
print(minMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"]))  # 出力: 1

# スタート遺伝子 "AACCGGTT" からエンド遺伝子 "AAACGGTA" への変異は2ステップで可能
# "AACCGGTT" -> "AACCGGTA" -> "AAACGGTA"
print(minMutation("AACCGGTT", "AAACGGTA", ["AACCGGTA", "AACCGCTA", "AAACGGTA"]))  # 出力: 2
