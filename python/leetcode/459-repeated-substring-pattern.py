# title: 459-repeated-substring-pattern.py
# by: Abhay Gupta
# date: 23-08-21
#
# desc: Given a string s, check if it can be constructed 
# by taking a substring of it and appending multiple 
# copies of the substring together.
#
# Leetcode || difficulty: Easy


class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:

    # find factors of the length of string
    total = len(s)
    factors = []

    # find factors of length of string
    for i in range(1, total+1):
      if (total/i).is_integer():
        factors.append(i)
    
    # loop through string & check if each substring is feasible
    for i in factors:
      for j in range(1,len(s)):
        clone = ""
        current = s[i:i+j] 
        if (len(s)/j).is_integer():
          for k in range(int(len(s)/j)):
            clone += current
          if clone == s:
            return True

    return False
                                        

