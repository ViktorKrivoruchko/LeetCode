# через два указателя
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            else:
                min_profit = prices[i] - min_price
                if min_profit > max_profit:
                    max_profit = min_profit
        return max_profit