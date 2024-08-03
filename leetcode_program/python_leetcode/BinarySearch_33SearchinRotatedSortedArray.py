from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # numsが空の場合、-1を返す
        if not nums:
            return -1
        # 配列の左端と右端のインデックスを初期化
        left, right = 0, len(nums) - 1
        # left が right 以下である限りループを続ける
        while left <= right:
            # 中間インデックスを計算
            mid = (left + right) // 2
            # 中間インデックスの値がターゲットと一致する場合、そのインデックスを返す
            if nums[mid] == target:
                return mid
            # 左半分がソートされている場合
            if nums[left] <= nums[mid]:
                # ターゲットが左半分に存在する場合、右端を mid - 1 に更新
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                # ターゲットが左半分に存在しない場合、左端を mid + 1 に更新
                else:
                    left = mid + 1
            # 右半分がソートされている場合
            else:
                # ターゲットが右半分に存在する場合、左端を mid + 1 に更新
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                # ターゲットが右半分に存在しない場合、右端を mid - 1 に更新
                else:
                    right = mid - 1
        # ターゲットが見つからなかった場合、-1 を返す
        return -1

# 使用例
# インスタンスの作成
solution = Solution()
# 配列 [4, 5, 6, 7, 0, 1, 2] の中で 0 を探す（期待される出力は 4）
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
print(solution.search(nums, target))  # 出力: 4
# 配列 [4, 5, 6, 7, 0, 1, 2] の中で 3 を探す（期待される出力は -1）
nums = [4, 5, 6, 7, 0, 1, 2]
target = 3
print(solution.search(nums, target))  # 出力: -1

# 配列 [1] の中で 0 を探す（期待される出力は -1）
nums = [1]
target = 0
print(solution.search(nums, target))  # 出力: -1
