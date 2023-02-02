class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #First step is filter the string to only letters 
        #After filtered, check is a valid palindrome is straight foward
        range_lowercase = range(ord("a"), ord("z")) #This is the range in ASCII of the lowercase letters
        range_numbers = range(ord("0"), ord("9"))
        s = s.lower() #convert the uppercase to lowercase
        cleaned_string = ""
        for char in s: 
            if ord(char) in range_lowercase: 
                cleaned_string += char
            elif ord(char) in range_numbers:
                cleaned_string += char
        #After filtred, the string can be checked for a palindrome
        s = cleaned_string
        print(cleaned_string)
        if (len(s)%2) == 0: 
            left = len(s) / 2 - 1
            right = left + 1
        elif (len(s)%2) != 0:
            left = len(s) // 2
            right = left

        while left >= 0 and right < len(s):
            if s[left] != s[right]: 
                return False
            left -= 1
            right += 1
        return True

s = "1a2"
ans = Solution.isPalindrome(s, s)
print(ans)