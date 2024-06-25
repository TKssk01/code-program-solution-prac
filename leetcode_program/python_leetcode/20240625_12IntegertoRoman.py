class Solution:
    def intToRoman(self, num: int) -> str:
        # ローマ数字のシンボルと値のペアを大きい順に定義する
        val = [
            1000,900,500,400,100,90,50,40,10,9,5,4,1
        ]
        syb = [
            "M","CM","D","CD","C","XC","L","XL","X","IX","V","IV","I"
        ]

        #結果の配列を初期化
        roman_num = ''
        i = 0

        # 入力値が0になるまで繰り返す
        # while num > 0:
        #     if val[i] <= num:
        #         roman_num += syb[i]
        #         num -= val[i]
        #     else:
        #         i += 1


        while num > 0:
        # 現在の値を入力値から引けるだけ引く
            for _ in range(num // val[i]):
                roman_num += syb[i]
                num -= val[i]
            i += 1
    
        return roman_num