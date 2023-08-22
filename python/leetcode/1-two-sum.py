# filename: 1-two-sum.py
# by: Abhay Gupta
# date: 23-08-21
#
# description: Given an array of integers nums and an integer target, 
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, 
# and you may not use the same element twice.


class Solution:

  def twoSum(self, nums: List[int], target: int) -> List[int]:
  
  # better by only including previous values for search
  # shortest possible imo
  prev = {}
  for c, i in enumerate(nums):
    if (target - i) in prev:
      return (c, prev[target - i])
    prev[i] = c


  # shortest solution that I could think of O(n)
  hashmap = {}
  for c, i in enumerate(nums):
    hashmap[i] = c

  for c, i in enumerate(nums):
    if (z := hashmap.get(target - i)):
      if (z-c):
        return (c,z)

  # check create a hashmap of expected adjacent pair and its index
  # memory large because you keep the index of repeats [unnecessary]
  # runtime: O(n)
  hashmap = {}
  for c, i in enumerate(nums):
    hashmap[i] = [c] + hashmap.get(i, [-1])

  for c, i in enumerate(nums):
    if (target - i) in hashmap:
      for j in hashmap[target - i]:
        if c != j and j >= 0:
          return (j, c)

  # optimized to use half the array 
  # runtime: [n], [n-1] ..... 1 + 2 + 3 ... + n = n(n + 1)/2 = n**2
    
    for c,i in enumerate(nums):
      for d,j in enumerate(nums):
        if c != d:
          if i + j == target:
            return [c,d]

  # brute force solution
  def twoSum(self, nums: List[int], target: int) -> List[int]:
      
    for c,i in enumerate(nums):
      for d,j in enumerate(nums):
        if c != d:
          if i + j == target:
            return [c,d
