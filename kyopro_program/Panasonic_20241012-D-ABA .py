def count_palindromic_triples(S):
  """
    from collections import defaultdict

    # 文字ごとの出現位置を記録（1-based index）
    char_positions = defaultdict(list)
    for idx, c in enumerate(S, 1):
        char_positions[c].append(idx)

    total = 0
    for c, positions in char_positions.items():
        m = len(positions)
        if m < 2:
            continue

        # 累積和を計算
        prefix_sum = [0] * m
        prefix_sum[0] = positions[0]
        for i in range(1, m):
            prefix_sum[i] = prefix_sum[i-1] + positions[i]

        # 各ペアからの貢献を計算
        for b in range(1, m):
            # positions[b]は1-based
            contribution = (b) * positions[b] - prefix_sum[b-1] - b
            total += contribution

    return total

  """
    