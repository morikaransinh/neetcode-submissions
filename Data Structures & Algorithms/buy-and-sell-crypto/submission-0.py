class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        MaxProfit = 0
        BestBuy = prices[0]
        for i in range(1,len(prices)):
            if(prices[i]>BestBuy):
                MaxProfit = max(MaxProfit,prices[i]-BestBuy)
            BestBuy=min(BestBuy,prices[i])

        return MaxProfit

        