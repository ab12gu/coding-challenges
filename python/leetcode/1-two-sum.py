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

        hashmap = {}

        for i in range(len(nums)):
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            hashmap[target - nums[i]] = 
