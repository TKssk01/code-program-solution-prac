from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # 最終結果を格納するリスト
        result = []
        # 現在の行に含まれる単語を格納するリスト
        current_line = []
        # 現在の行の文字数を追跡する変数
        current_length = 0 
        for word in words:
            # 単語を追加した場合にmaxWidthを超えるかどうかを確認
            if current_length + len(current_line) + len(word) > maxWidth:
                # maxWidthを超える場合、現在の行を整形して結果に追加
                for i in range(maxWidth - current_length):
                    # 空白を均等に分配する
                    current_line[i % (len(current_line) - 1 or 1)] += ' '
                # 整形した行を結果リストに追加
                result.append(''.join(current_line))
                # 新しい行を開始するためにリセット
                current_line = []
                current_length = 0
            # 現在の行に単語を追加
            current_line.append(word)
            # 現在の行の文字数を更新
            current_length += len(word)
        # 最後の行は左揃えにして結果に追加
        result.append(' '.join(current_line).ljust(maxWidth))
        return result