'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
'''

class Solution(object):
  def is_valid(self, s):
      """
      :type s: str
      :rtype: bool
      """
      stc = []
      #Relations between different types of parentheses
      map = {")": "(", "]": "[", "}": "{"}
      for c in s: 
        #If c is a open parentheses, add to stack
        if c not in map: 
          stc.append(c)
        #Else, verify if the top of stack is a open parentheses that have a relation with c
        else: 
          if stc and stc[-1] == map[c]: 
            stc.pop()
          else: 
            return False
       if len(stc) == 0: 
         return True 
       else: 
         return False
        
  
