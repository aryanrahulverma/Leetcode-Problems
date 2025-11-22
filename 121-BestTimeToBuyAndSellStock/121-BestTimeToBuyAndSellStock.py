# Last updated: 11/21/2025, 8:46:46 PM
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        n = len(prices)

        if n == 1:
            return 0
        
        s, e = 0, 1

        while e < n:
            if prices[e] < prices[s]:
                s = e
                e += 1
            else:
                profit = max(profit, prices[e] - prices[s])
                e += 1

        return profit
