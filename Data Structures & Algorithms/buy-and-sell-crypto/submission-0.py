class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r=0,1
        pr=0
        while r<len(prices):
            if(prices[r]<prices[l]):
                l=r
            if(prices[l]<prices[r]):
                profit=prices[r]-prices[l]
                pr=max(profit,pr)
            r+=1
        return pr