class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        vals=[float("inf")]*(amount+1)
        vals[0]=0

        for i in range(1,amount+1):
            for coin in coins:
                if coin<=i:
                    vals[i]=min(vals[i],1+vals[i-coin])

        return vals[amount] if vals[amount] != float('inf') else -1 