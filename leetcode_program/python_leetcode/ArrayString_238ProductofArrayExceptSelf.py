from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # nums_temp = 1
        # nums_new = []
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if i != j:
        #             # print(nums[j])
        #             nums_temp *= nums[j]
        #         else:
        #             continue
        #     nums_new.append(nums_temp)
        #     nums_temp = 1
        # return nums_new

        n = len(nums)  # n = 4
        left_products = [1] * n  # left_products = [1, 1, 1, 1]
        right_products = [1] * n  # right_products = [1, 1, 1, 1]
        result = [1] * n  # result = [1, 1, 1, 1]

        for i in range(1,n):
            left_products[i] = left_products[i-1] * nums[i-1]
        # 具体的な計算ステップ
        # i = 1: left_products[1] = left_products[0] * nums[0] = 1 * 1 = 1  => left_products = [1, 1, 1, 1]
        # i = 2: left_products[2] = left_products[1] * nums[1] = 1 * 2 = 2  => left_products = [1, 1, 2, 1]
        # i = 3: left_products[3] = left_products[2] * nums[2] = 2 * 3 = 6  => left_products = [1, 1, 2, 6]
        
        for i in range(n-2,-1,-1):
            right_products[i] = right_products[i+1] * nums[i+1]

        # 具体的な計算ステップ
        # i = 2: right_products[2] = right_products[3] * nums[3] = 1 * 4 = 4  => right_products = [1, 1, 4, 1]
        # i = 1: right_products[1] = right_products[2] * nums[2] = 4 * 3 = 12 => right_products = [1, 12, 4, 1]
        # i = 0: right_products[0] = right_products[1] * nums[1] = 12 * 2 = 24 => right_products = [24, 12, 4, 1]

        for i in range(n):
            result[i] = left_products[i] * right_products[i]

        # 具体的な計算ステップ
        # i = 0: result[0] = left_products[0] * right_products[0] = 1 * 24 = 24  => result = [24, 1, 1, 1]
        # i = 1: result[1] = left_products[1] * right_products[1] = 1 * 12 = 12  => result = [24, 12, 1, 1]
        # i = 2: result[2] = left_products[2] * right_products[2] = 2 * 4 = 8    => result = [24, 12, 8, 1]
        # i = 3: result[3] = left_products[3] * right_products[3] = 6 * 1 = 6    => result = [24, 12, 8, 6]
        
        return result
    
if __name__ == "__main__":
    solution = Solution()

    # テストケース
    test_cases = [
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([4, 5, 1, 8, 2], [80, 64, 320, 40, 160]),
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([0, 1, 2, 3], [6, 0, 0, 0]),
        ([1, 2, 3, 0], [0, 0, 0, 6]),
    ]

    for nums, expected in test_cases:
        result = solution.productExceptSelf(nums)
        print(f"nums: {nums}, expected: {expected}, got: {result}, pass: {result == expected}")