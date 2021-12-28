##
# name: Search_Insertion_Position.py
# by: Abhay Gupta
#
# date: 02-17-20
# desc: Given a sorted array and target, return target's desired location in array
from typing import List


class Solution:
    def __init__(self):
        pass

    def searchInsert(self, nums, target):

        # Let's do a binary search

        high = len(nums) - 1
        low = 0
        mid = int((high + low) / 2)

        if target > nums[high]:
            return high + 1
        if target < nums[low]:
            return low

        while (low <= high):
            print(mid)
            if target == nums[mid]:
                return mid
            if mid == low:
                return high
            if mid == high:
                return low
            if target > nums[mid]:
                low = mid
            else:
                high = mid

            mid = int((low + high) / 2)

        return low

if __name__ == '__main__':

    nums = [1, 3, 5, 6]
    target = 2

    s = Solution() # Create instance of a class
    s.searchInsert(nums, target) # Call method