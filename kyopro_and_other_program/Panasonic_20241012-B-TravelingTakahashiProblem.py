"""
https://atcoder.jp/contests/abc375/tasks/abc375_b

問題文
2 次元座標平面の原点に高橋くんがいます。

高橋くんが座標平面上の点 
(a,b) から点 
(c,d) に移動するには 
(a−c) 
2
 +(b−d) 
2
 
​
  のコストがかかります。

高橋くんが原点からスタートし 
N 個の点 
(X 
1
​
 ,Y 
1
​
 ),…,(X 
N
​
 ,Y 
N
​
 ) へこの順に移動したのち原点に戻るときの、コストの総和を求めてください。

制約
1≤N≤2×10 
5
 
−10 
9
 ≤X 
i
​
 ,Y 
i
​
 ≤10 
9
 
入力は全て整数である
入力
入力は以下の形式で標準入力から与えられる。

N
X 
1
​
  
Y 
1
​
 
⋮
X 
N
​
  
Y 
N
​
 
出力
答えを出力せよ。
真の値との相対誤差または絶対誤差が 
10 
−6
  以下であれば正解とみなされる。

入力例 1
Copy
2
1 2
-1 0
出力例 1
Copy
6.06449510224597979401
移動は次の 
3 行程からなります。

(0,0) から 
(1,2) に移動する。
(0−1) 
2
 +(0−2) 
2
 
​
 = 
5
​
 =2.236067977... のコストがかかる
(1,2) から 
(−1,0) に移動する。
(1−(−1)) 
2
 +(2−0) 
2
 
​
 = 
8
​
 =2.828427124... のコストがかかる
(−1,0) から 
(0,0) に移動する。
(−1−0) 
2
 +(0-0) 
2

1

 =1 のコストがかかる
コストの総和は 
6.064495102... となります。

"""

import sys
import os


def main():
    count = 0
    import math
    
    input = sys.stdin.read
    data = input().split()
    
    N = int(data[0])
    coords = []
    
    for i in range(N):
        X = int(data[1+2*i])
        Y = int(data[2+2*i])
        coords.append((X,Y))
        
    total_cost = 0.0
    prev_x, prev_y = 0,0
    
    for(x,y) in coords:
        dx = x - prev_x
        dy = y - prev_y
        distance = math.hypot(dx,dy)
        total_cost += distance
        
        prev_x, prev_y = x,Y
        
    dx = 0 - prev_x
    dy = 0 - prev_y
    distance = math.hypot(dx,dy)
    total_cost += distance
    
    print("{0:.20f}".format(total_cost))
    
if __name__ == "__main__":
    main()