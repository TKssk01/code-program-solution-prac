from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # ベースケース：numsが空の場合、空のリストのリストを返す
        if len(nums) == 0:
            return [[]]
        # 結果を格納するリスト
        result = []
        # numsの各要素を固定して順列を生成
        for i in range(len(nums)):
            # nums[i]を除いた残りの要素で再帰的に順列を生成
            rest = nums[:i] + nums[i+1:]
            # 再帰呼び出し
            for p in self.permute(rest):
                # nums[i]を前に追加して新しい順列を作成
                result.append([nums[i]] + p)
        return result

# テストケース
solution = Solution()
nums1 = [1, 2, 3]
nums2 = [0, 1]
nums3 = [1]

# 結果を表示
print(solution.permute(nums1))  # [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
print(solution.permute(nums2))  # [[0, 1], [1, 0]]
print(solution.permute(nums3))  # [[1]]
