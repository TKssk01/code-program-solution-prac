# 必要なモジュールをインポート
from collections import defaultdict
from math import gcd
from typing import List
# Solution クラスの定義
class Solution:
    # maxPoints メソッドの定義。入力は点のリスト。
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)  # 点の数を取得
        if n < 3:  # 点が2つ以下の場合、その点数が答えになる
            return n
        # 2点間の傾きを計算する補助関数
        def slope(p1, p2):
            dx = p2[0] - p1[0]  # x座標の差を計算
            dy = p2[1] - p1[1]  # y座標の差を計算
            if dx == 0:  # x座標の差が0の場合、垂直線になる
                return (0, 1)
            if dy == 0:  # y座標の差が0の場合、水平線になる
                return (1, 0)
            d = gcd(dx, dy)  # x座標とy座標の差の最大公約数を求める
            # 正規化: 傾きを一意に決めるため、符号を統一する
            dx //= d  # x座標の差を最大公約数で割る
            dy //= d  # y座標の差を最大公約数で割る
            if dx < 0:  # dxが負の場合、符号を反転して統一
                dx = -dx
                dy = -dy
            return (dy, dx)  # 正規化された傾きをタプルで返す
        max_points = 1  # 最大の点数を記録する変数を初期化
        # 各点を基準点としてループを回す
        for i in range(n):
            slopes = defaultdict(int)  # 傾きごとに点数をカウントするための辞書を初期化
            same_point_count = 0  # 同じ位置にある点の数をカウントする変数
            local_max = 0  # 現在の基準点における最大の点数を初期化
            # 基準点以外の点との組み合わせを調べる
            for j in range(i + 1, n):
                if points[i] == points[j]:  # 基準点と同じ位置にある点を見つけた場合
                    same_point_count += 1  # 同じ位置の点をカウント
                    continue  # 同じ位置の点は無視して次へ進む
                s = slope(points[i], points[j])  # 基準点と他の点との傾きを計算
                slopes[s] += 1  # 辞書にその傾きでカウントを増やす
                local_max = max(local_max, slopes[s])  # ローカル最大値を更新する
            # 基準点を含めて、同じ直線上にある点の数の最大値を更新
            max_points = max(max_points, local_max + same_point_count + 1)
        return max_points  # 最大の点数を返す
# テストケース
solution = Solution()  # Solutionクラスのインスタンスを作成
points1 = [[1,1],[2,2],[3,3]]  # 直線上にある3つの点
points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]  # 最大で4つの点が同一直線上にある点群
# 結果の出力
print(solution.maxPoints(points1))  # 出力: 3
print(solution.maxPoints(points2))  # 出力: 4
