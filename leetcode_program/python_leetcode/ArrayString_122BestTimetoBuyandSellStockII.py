class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if len(prices) <= 1:
        #     return 0
        # #121. Best Time to Buy and Sell Stock Iのコード
        # max_profit = 0
        # min_price = prices[0]
        # for price in prices[1:]:
        #     if price < min_price:
        #         min_price = price
        #     else:
        #         max_profit = max(max_profit, price - min_price)


        # return max_profit
    
        #122. Best Time to Buy and Sell Stock IIのコード

        difference_profit = 0

        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                difference_profit += prices[i] - prices[i-1]
            else:
                continue
        
        return difference_profit