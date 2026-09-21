class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float("inf")]*(amount+1)
        dp[0]=0

        for current_am in range(1,amount+1):
            for i in coins:
                if current_am>=i:
                    dp[current_am]=min(dp[current_am],1+dp[current_am-i])
        if(dp[amount]==float("inf")):
            return -1
        else:
            return dp[amount]