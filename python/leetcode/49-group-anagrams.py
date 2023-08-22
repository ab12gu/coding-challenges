# filename: 49-group-anagrams.py
# by: Abhay Gupta
# date: 23-08-22
# 
# desc: Given an array of strings strs, group the anagrams together. 
# You can return the answer in any order.
#
# An Anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase, typically using all the original letters exactly once.

class Solution: 
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

    output = []
    table = {}
    size = 0

    for s in strs:
      anagram = sorted(list(s))
      anagram = int(''.join(["1"] + [str(ord(x)) for x in anagram]))

      if anagram in table:
        output[table[anagram]].append(s)
      else:
        table[anagram] = size
        size += 1
        output.append([s])

    return output

