# filename: 242-valid-anagram.py
# by: Abhay Gupta
# date: 23-08-21
#
# descrption: Given two strings s and t, return true 
# if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging 
# the letters of a different word or phrase, typically 
# using all the original letters exactly once.
##



class Solution:
  def isAnagram(self, s: str, t: str) -> bool:

    s_map = [0] * 26
    t_map = [0] * 26
    size = len(s)

    if len(s) != len(t):
      return False

    for i in range(size):
      s_map[ord(s[i]) - 97] += 1
      t_map[ord(t[i]) - 97] += 1

    for i in range(26):
      if s_map[i] != t_map[i]:
        return False
    
    return True

