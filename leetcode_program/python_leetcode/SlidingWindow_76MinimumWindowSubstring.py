from collections import Counter

def min_window(s: str, t: str) -> str:
    # s または t が空の場合は、空文字列を返す
    if not t or not s:
        return ""
    # t の各文字の出現回数をカウントして、dict_t に格納
    dict_t = Counter(t)
    # t に含まれる異なる文字の種類数をカウント
    required = len(dict_t)
    # 左右のポインタを初期化
    l, r = 0, 0
    # formed は、現在のウィンドウが条件を満たしている文字数
    formed = 0
    # 現在のウィンドウ内の文字カウントを保持する辞書
    window_counts = {}
    # 最小ウィンドウの長さとその開始・終了位置を保持する
    ans = float("inf"), None, None
    # 右ポインタ r が文字列 s の終わりまで移動する
    while r < len(s):
        # 現在の文字を取得
        character = s[r]
        # window_counts に現在の文字を追加または更新
        window_counts[character] = window_counts.get(character, 0) + 1
        # もし現在の文字が t に含まれており、そのカウントが t で要求される数と一致する場合
        if character in dict_t and window_counts[character] == dict_t[character]:
            # formed を増加させる
            formed += 1
        # 左ポインタ l を右に移動させながら、ウィンドウが条件を満たしている間はサイズを縮小
        while l <= r and formed == required:
            # ウィンドウの左端の文字を取得
            character = s[l]
            # 現在のウィンドウが最小のものかを確認し、更新
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
            # ウィンドウ内の左端の文字のカウントを減らす
            window_counts[character] -= 1
            # もしこの文字が t に含まれ、かつ現在のウィンドウでのカウントが t で要求される数より少ない場合
            if character in dict_t and window_counts[character] < dict_t[character]:
                # formed を減少させる
                formed -= 1
            # 左ポインタを右に移動
            l += 1    
        # 右ポインタを右に移動
        r += 1    
    # 最小ウィンドウが見つかった場合はその文字列を、見つからなかった場合は空文字列を返す
    return "" if ans[0] == float("inf") else s[ans[1]: ans[2] + 1]
# テストケース
print(min_window("ADOBECODEBANC", "ABC"))  # 出力: "BANC"
print(min_window("a", "a"))  # 出力: "a"
print(min_window("a", "aa"))  # 出力: ""
