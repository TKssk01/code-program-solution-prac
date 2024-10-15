def count_characters_and_words(input_string):
    """
    文字列を入力として、特殊文字およびスペースを除いた文字カウントと
    ワードカウントを返す関数。

    Args:
        input_string (str): 入力文字列 (1文字以上10^5文字以内)

    Returns:
        dict: {
            "characters": int,  # 特殊文字とスペースを除いた文字数
            "words": int        # 単語数
        }
    """
    # 文字カウント: アルファベットと数字のみをカウント
    character_count = sum(1 for c in input_string if c.isalnum())

    # ワードカウント: スペースで分割した単語の数をカウント
    # str.split() はデフォルトで任意の長さの空白文字を区切りとして扱う
    words = input_string.strip().split()
    word_count = len(words)

    return {
        "characters": character_count,
        "words": word_count
    }

# ### 使用例 ###

# 入力例
input_example = "I have a nice question"

# 関数の呼び出し
result = count_characters_and_words(input_example)

# 結果の表示
print(result)  # 出力: {'characters': 18, 'words': 5}