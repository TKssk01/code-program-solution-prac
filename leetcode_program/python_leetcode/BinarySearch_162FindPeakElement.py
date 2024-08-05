from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # 初期設定: leftは配列の最初のインデックス、rightは配列の最後のインデックスを指す
        left, right = 0, len(nums) - 1
        # leftがrightより小さい間ループを続ける
        while left < right:
            # 中央のインデックスを計算
            mid = (left + right) // 2
            # 中央の要素がその右隣の要素より大きい場合
            if nums[mid] > nums[mid + 1]:
                # 右側の範囲を左側に縮小
                right = mid
            else:
                # 左側の範囲を右側に縮小
                left = mid + 1
        # ループが終了した時点でleftがピーク要素のインデックスを指している
        return left
# 使用例
nums1 = [1, 2, 3, 1]
nums2 = [1, 2, 1, 3, 5, 6, 4]

# Solutionクラスのインスタンスを作成
solution = Solution()

# 結果の出力
print(solution.findPeakElement(nums1))  # 出力: 2
print(solution.findPeakElement(nums2))  # 出力: 5 または 1
