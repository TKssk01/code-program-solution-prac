class Solution:
    def jump(self, nums: List[int]) -> int:
        # if len(nums) == 1:
        #     return 1
        # if nums[0] == 0:
        #     return False
    
        # max_reach = nums[0]
        # count = 0
        # for i in range(1, len(nums)):
        #     if i > max_reach:
        #         return False
        #     max_reach = max(max_reach, i + nums[i])
        #     if max_reach >= len(nums) - 1:
        #         count += 1
        #         return count
        # return False

        # 配列の長さが1の場合、ジャンプは不要なので0を返す
        if len(nums) == 1:
            return 0
        # 最初の位置から到達可能な最遠のインデックスを初期化
        max_reach = nums[0]
        # 現在のジャンプで残りのステップ数を初期化
        steps = nums[0]
        # 行ったジャンプの回数を初期化（最初のジャンプとして1回をカウント）
        jumps = 1
        # 配列の2番目の要素から最後までイテレート
        for i in range(1, len(nums)):
            # 最後の要素に到達した場合、ジャンプ回数を返す
            if i == len(nums) - 1:
                return jumps
            # 現在のインデックスから到達可能な最遠のインデックスを更新
            max_reach = max(max_reach, i + nums[i])
            # 残りのステップ数を1減らす
            steps -= 1
            # 残りのステップ数が0になった場合
            if steps == 0:
                # ジャンプ回数を1増やす
                jumps += 1
                # 現在の位置からの最大到達範囲を新たなステップ数として設定
                steps = max_reach - i
        # 最後のインデックスに到達したときのジャンプ回数を返す
        return jumps