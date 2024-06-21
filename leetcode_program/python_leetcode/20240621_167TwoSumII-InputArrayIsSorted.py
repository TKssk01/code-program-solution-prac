class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # 数値からそのインデックスを取得するための辞書
        num_to_index = {}
        # numbersリストの各要素とそのインデックスを列挙
        for index, number in enumerate(numbers):
            # 対象となるターゲットから現在の数値を引いて補数を計算
            complement = target - number
            # 補数が既に辞書に存在するかどうかを確認
            if complement in num_to_index:
                # 存在する場合、そのインデックス（1始まり）と現在のインデックス（1始まり）を返す
                return [num_to_index[complement] + 1, index + 1]
            # 辞書に現在の数値とそのインデックスを追加
            num_to_index[number] = index
        # 適合するペアが見つからなかった場合、Noneを返す
        return None
