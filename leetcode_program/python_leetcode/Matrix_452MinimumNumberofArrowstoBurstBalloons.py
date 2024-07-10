from typing import List

def findMinArrowShots(points):
    # 入力が空の場合、必要な矢の数は0
    if not points:
        return 0
    # 風船を終点(xend)でソート
    # lambda関数を使用して、各要素の2番目の値（終点）でソート
    points.sort(key=lambda x: x[1])
    # 必要な矢の数を初期化（最低1本は必要）
    arrows = 1
    # 最初の風船の終点を現在の矢の位置とする
    end = points[0][1]
    # 2番目の風船から順にチェック
    for i in range(1, len(points)):
        # 現在の風船の開始点が、前の矢の位置より後ろにある場合
        if points[i][0] > end:
            # 新しい矢が必要なので、カウントを増やす
            arrows += 1
            # 新しい矢の位置を現在の風船の終点に更新
            end = points[i][1]
    # 必要な矢の総数を返す
    return arrows