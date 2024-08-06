class MedianFinder:

    def __init__(self):
        # リストを初期化
        self.nums = []

    def addNum(self, num: int) -> None:
        # 数字をリストに追加
        self.nums.append(num)
        # リストをソート
        self.nums.sort()

    def findMedian(self) -> float:
        # リストの長さを取得
        n = len(self.nums)
        if n % 2 == 1:
            # リストのサイズが奇数の場合、中央の値を返す
            return self.nums[n // 2]
        else:
            # リストのサイズが偶数の場合、中央の二つの値の平均を返す
            mid1 = self.nums[n // 2 - 1]
            mid2 = self.nums[n // 2]
            return (mid1 + mid2) / 2.0

# 使用例
medianFinder = MedianFinder()
medianFinder.addNum(1)       # リスト: [1]
medianFinder.addNum(2)       # リスト: [1, 2]
print(medianFinder.findMedian())  # 中央値: 1.5
medianFinder.addNum(3)       # リスト: [1, 2, 3]
print(medianFinder.findMedian())  # 中央値: 2.0



# import heapq

# class MedianFinder:

#     def __init__(self):
#         # 最大ヒープを使うためのリスト（小さい値を格納）
#         self.small = []
#         # 最小ヒープを使うためのリスト（大きい値を格納）
#         self.large = []

#     def addNum(self, num: int) -> None:
#         # largeに新しい数を追加し、最小の要素をsmallに移動
#         heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
#         # smallのサイズがlargeのサイズを超える場合、要素をlargeに移動
#         if len(self.small) > len(self.large):
#             heapq.heappush(self.large, -heapq.heappop(self.small))

#     def findMedian(self) -> float:
#         # largeのサイズがsmallのサイズを超える場合、largeの最小要素を返す
#         if len(self.large) > len(self.small):
#             return float(self.large[0])
#         # そうでない場合、largeの最小要素とsmallの最大要素の平均を返す
#         return (self.large[0] - self.small[0]) / 2.0

