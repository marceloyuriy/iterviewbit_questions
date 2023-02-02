#Coin Change problem
#The idea here is use the previous values to calculate the next values
#
class Solution: 
    def solve(self, coins, amount): #A represents the coins and B represent the sum 
        dp = [amount+1] * (amount + 1) #This value of b+1 represents one number to greater than all the elements. 
        dp[0] = 0
        for a in range(1, amount + 1): 
            for c in coins: 
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-c])
        return dp[amount] if dp[amount] != amount +1 else -1
        
#Main function to call the solution class
A = [1,2,5,9,8]
B = 17
bag_coins = Solution.solve(A,A,B)
print(bag_coins)
'''Time complexity and space complexity
Time: O(amount * len(coins))
Space: O(amount)