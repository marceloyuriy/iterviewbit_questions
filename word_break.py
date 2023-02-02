#Word Break 
#The statement of this problem starts telling us about string s, but 
#the ideia to solve this problem starts thinking on dictionary. 
#Instead of looking for every letter of string and search such correspondence
#with dictionary word, search for each word of the dictionary in the string. 
#Additionally, the dynamic programming will go through the string in reverse order. 
class Solution: 
    def wordBreak (self, s, wordDict):
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]
                    