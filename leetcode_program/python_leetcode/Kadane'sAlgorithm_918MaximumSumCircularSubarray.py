def maxSubarraySumCircular(nums):
    # Kadane'sアルゴリズムを使って最大部分配列の和を見つける関数
    def kadane(nums):
        # 最初の要素でmax_sumとcurrent_sumを初期化
        max_sum = current_sum = nums[0]
        # 残りの要素を順に処理
        for num in nums[1:]:
            # current_sumを現在の要素またはcurrent_sum + 現在の要素のどちらか大きい方に更新
            current_sum = max(num, current_sum + num)
            # max_sumをmax_sumまたはcurrent_sumのどちらか大きい方に更新
            max_sum = max(max_sum, current_sum)
        return max_sum

    # 配列全体の合計を計算
    total_sum = sum(nums)
    
    # Kadane'sアルゴリズムを使って非循環配列の最大部分配列の和を求める
    max_kadane = kadane(nums)
    
    # 非循環配列の最小部分配列の和を見つける
    # Kadane'sアルゴリズムを利用するために配列の各要素の符号を反転
    for i in range(len(nums)):
        nums[i] = -nums[i]
    
    # 反転した配列でKadane'sアルゴリズムを使って最大部分配列の和を求める（元の配列の最小部分配列の和に相当）
    max_inverse_kadane = kadane(nums)
    
    # 配列の元の値を戻すために符号を再度反転
    for i in range(len(nums)):
        nums[i] = -nums[i]
    
    # すべての数が負の場合、max_inverse_kadaneは-total_sumに等しくなる
    if max_inverse_kadane == -total_sum:
        # 非循環配列で見つけた最大部分配列の和を返す
        return max_kadane
    
    # 循環配列における最大部分配列の和を計算
    max_circular = total_sum + max_inverse_kadane
    
    # 2つの結果、max_kadaneとmax_circularのうち大きい方を返す
    return max(max_kadane, max_circular)

# 使用例
nums1 = [1, -2, 3, -2]
nums2 = [5, -3, 5]
nums3 = [-3, -2, -3]

# 各例の配列に対する関数の結果を表示
print(maxSubarraySumCircular(nums1))  # 出力: 3
print(maxSubarraySumCircular(nums2))  # 出力: 10
print(maxSubarraySumCircular(nums3))  # 出力: -2
