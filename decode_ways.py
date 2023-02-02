#Decode Ways

class Solution: 
    def decodeWays (self, s):
        #Iterative method
        dp = {len (s) : 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else: 
                dp[i] = dp[i+1]
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]
        return dp[0]
        #Recusive method
        dp = { len(s) : 1}
        def dfs(i):
             if i in dp: 
                 return dp[i] #Saving the previous results
             if s[i] == "0":
                 return 0 #Zero cannot represent a letter
             res = dfs(i+1) #First case, only one digit
             if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                 res += dfs(i + 2) #Second case, considering the second digit
             dp[i] = res
             return res
        return dfs(0)
    
A = "121"
ans = Solution.decodeWays(A, A)
print (ans)
