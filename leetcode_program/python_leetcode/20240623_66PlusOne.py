from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # リストの最後の要素から順に処理を開始
        for i in range(len(digits)-1, -1, -1):
            # 現在の桁が9である場合
            if digits[i] == 9:
                # 現在の桁を0に設定
                digits[i] = 0
                # もし最初の桁であれば、先頭に1を挿入
                if i == 0:
                    digits.insert(0, 1)
            else:
                # 9でなければ、その桁を1増やし、処理を終了
                digits[i] += 1
                break
        # 更新されたリストを返す
        return digits

# テストケース
if __name__ == "__main__":
    solution = Solution()
    digits = [1,2,3]
    print(solution.plusOne(digits))
    digits = [9]
    print(solution.plusOne(digits))
    digits = [9,9]
    print(solution.plusOne(digits))
