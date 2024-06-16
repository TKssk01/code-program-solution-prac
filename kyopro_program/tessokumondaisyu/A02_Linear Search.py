# 問題文
# N 個の整数 A_1, A_2, \cdots, A_N の中に、整数 X が含まれるかどうかを判定するプログラムを作成してください。

# 制約
# N は 1 以上 100 以下の整数
# X は 1 以上 100 以下の整数
# A_1, A_2, \cdots, A_N は 1 以上 100 以下の整数
# 入力
# 入力は以下の形式で標準入力から与えられます。

# N X
# A_1 A_2 \cdots A_N
# 出力
# 整数 X が含まれるとき Yes、含まれないとき No と出力してください。

# 入力例 1
# 5 40
# 10 20 30 40 50
# 出力例 1
# Yes
# この入力例では、N=5, X=40, (A_1, A_2, A_3, A_4, A_5) = (10, 20, 30, 40, 50) となっています。
# A_4 の値が X と一致するため、Yes と出力すれば正解です。

# N, X = int(input().split()) # 入力
# A = list(map(int, input().split())) # 入力

# if X in A:
#     print("Yes")
# else:
#     print("No")

# N と X を空白区切りで入力
N, X = map(int, input().split())

# A のリストを入力
A = list(map(int, input().split()))

# X が A に含まれているかをチェック
if X in A:
    print("Yes")
else:
    print("No")
