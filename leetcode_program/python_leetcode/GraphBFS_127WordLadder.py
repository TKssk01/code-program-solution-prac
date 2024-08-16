from collections import deque  # dequeをインポート（BFSで使用）

def ladderLength(beginWord, endWord, wordList):
    # endWordがwordListにない場合、変換は不可能なので0を返す
    if endWord not in wordList:
        return 0
    # wordListをセットに変換して、探索と削除を高速化
    wordSet = set(wordList)
    # キューを作成し、開始単語とステップ数を追加（ステップ数は1から開始）
    queue = deque([(beginWord, 1)])
    # キューが空になるまでBFSを実行
    while queue:
        # キューから現在の単語とその時点でのステップ数を取り出す
        current_word, steps = queue.popleft()
        # 現在の単語の各文字を 'a' から 'z' に順番に変えて、新しい単語を生成
        for i in range(len(current_word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                next_word = current_word[:i] + c + current_word[i+1:]
                # 生成された単語がendWordなら、ステップ数に1を加えて返す
                if next_word == endWord:
                    return steps + 1
                # 生成された単語がwordSetに含まれている場合、次のステップに進む
                if next_word in wordSet:
                    # 探索済みの単語をセットから削除
                    wordSet.remove(next_word)
                    # 新しい単語とステップ数をキューに追加
                    queue.append((next_word, steps + 1))
    # キューが空になるまでendWordに到達しなかった場合、変換は不可能なので0を返す
    return 0
# 使用例:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
# 関数を呼び出して結果を表示（期待される出力は5）
print(ladderLength(beginWord, endWord, wordList))  # 出力: 5