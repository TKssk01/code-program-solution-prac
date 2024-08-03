def searchRange(nums, target):
    # 左側の境界を見つけるためのヘルパー関数
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1  # 左端を0、右端を配列の最後に設定
        while left <= right:  # 左端が右端を越えない限りループ
            mid = (left + right) // 2  # 中間位置を計算
            if nums[mid] < target:  # 中間位置の値がターゲットより小さい場合
                left = mid + 1  # 左端を中間位置の右側に設定
            else:  # 中間位置の値がターゲット以上の場合
                right = mid - 1  # 右端を中間位置の左側に設定
        return left  # 最終的な左端を返す
    # 右側の境界を見つけるためのヘルパー関数
    def findRight(nums, target):
        left, right = 0, len(nums) - 1  # 左端を0、右端を配列の最後に設定
        while left <= right:  # 左端が右端を越えない限りループ
            mid = (left + right) // 2  # 中間位置を計算
            if nums[mid] <= target:  # 中間位置の値がターゲット以下の場合
                left = mid + 1  # 左端を中間位置の右側に設定
            else:  # 中間位置の値がターゲットより大きい場合
                right = mid - 1  # 右端を中間位置の左側に設定
        return right  # 最終的な右端を返す
    left = findLeft(nums, target)  # 左側の境界を見つける
    right = findRight(nums, target)  # 右側の境界を見つける
    # 左端と右端が正しい範囲内でターゲットが存在する場合
    if left <= right and left < len(nums) and nums[left] == target and nums[right] == target:
        return [left, right]  # 開始位置と終了位置を返す
    return [-1, -1]  # ターゲットが存在しない場合は[-1, -1]を返す

# 使用例
print(searchRange([5,7,7,8,8,10], 8))  # 出力: [3, 4]
print(searchRange([5,7,7,8,8,10], 6))  # 出力: [-1, -1]
print(searchRange([], 0))              # 出力: [-1, -1]
