#Longest palindromic substring
#The idea behind this algorithm is go throught adjacencies elements 
#of each element of the string. For strings with odd number of entries
#we start from the same element, and for strings with even number of elements
#we star for adjacency elements. 
class Solution: 
    def longestPalindrome (self, s):
        res = ""
        resLen = 0
        
        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            #Even Length
            l, r = i, i+1
            while l >= 0 and r< len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
        
s = "babad"
ans = Solution.longestPalindrome(s, s)
print (ans)

#Palindromic substring
#The idea behind this question is almost the same of longest palindrome substring. 
#The main difference is calculate the number of total of palindrome insted of one palindrome. 
class Solution: 
    def PalindromeSubstring (self, s):
        count = 0
        
        for i in range(len(s)):
            #odd length
            l, r = i, i
            while l >= 0 and r< len(s) and s[l] == s[r]: #This while can be over
                count += 1
                l -= 1
                r += 1
            #Even Length
            l, r = i, i+1
            while l >= 0 and r< len(s) and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1
        return count
s = "babad"
ans = Solution.PalindromeSubstring (s, s)
print (ans)