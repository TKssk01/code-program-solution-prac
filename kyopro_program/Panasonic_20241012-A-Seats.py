"""
問題文

N 個の座席が並んでおり、座席には 
1,2,…,N の番号が付けられています。

座席の状態は #, . からなる長さ 
N の文字列 
S によって与えられます。
S の 
i 文字目が # のとき座席 
i には人が座っていることを表し、
S の 
i 文字目が . のとき座席 
i には人が座っていないことを表します。

1 以上 
N−2 以下の整数 
i であって、以下の条件を満たすものの個数を求めてください。

座席 
i,i+2 には人が座っており、座席 
i+1 には人が座っていない
制約
N は 
1 以上 
2×10 
5
  以下の整数
S は #, . からなる長さ 
N の文字列
入力
入力は以下の形式で標準入力から与えられる。

N
S
出力
答えを出力せよ。

入力例 1
Copy
6
#.##.#
出力例 1
Copy
2
i=1,4 が条件を満たすので、答えは 
2 です。

入力例 2
Copy
1
#
出力例 2
Copy
0
入力例 3
Copy
9
##.#.#.##
出力例 3
Copy
3

"""

import sys


def count_seats(N, S):
    count = 0
    
    for i in range(N - 2):
        if S[i] == '#' and S[i+1] == '.' and S[i+2] == '#':
            count += 1
    return count

if __name__ == "__main__":
    import sys
    #入力を受け取る
    N = int(sys.stdin.readline())
    S = sys.stdin.readline().strip()
    
    result = count_seats(N,S)
    print(result)