from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # AとBを設定 (常にAの方が短くなるようにする)
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A

        # AとBの長さを取得
        m, n = len(A), len(B)

        # 二分探索の初期値を設定
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        # 二分探索を開始
        while imin <= imax:
            # 中間インデックスを計算
            i = (imin + imax) // 2
            # Bにおける対応するインデックスを計算
            j = half_len - i

            # iが小さすぎる場合、iを増やす
            if i < m and B[j-1] > A[i]:
                imin = i + 1
            # iが大きすぎる場合、iを減らす
            elif i > 0 and A[i-1] > B[j]:
                imax = i - 1
            else:
                # iがちょうど良い場合
                # 左側の最大値を求める
                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                # 要素数が奇数の場合は、左側の最大値が中央値
                if (m + n) % 2 == 1:
                    return max_of_left

                # 右側の最小値を求める
                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                # 要素数が偶数の場合は、左側の最大値と右側の最小値の平均が中央値
                return (max_of_left + min_of_right) / 2.0

# 使用例
nums1 = [1, 3]
nums2 = [2]
solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))  # 2.0

nums1 = [1, 2]
nums2 = [3, 4]
print(solution.findMedianSortedArrays(nums1, nums2))  # 2.5
