# через два указателя
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        count_price = 0
        for price in prices:
            if min_price > price:
                min_price = price
            else:
                count_price += price - min_price
                min_price = price
        return count_price