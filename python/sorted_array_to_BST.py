##
# filename: sorted_array_to_BST.py
#
# by: Abhay Gupta
# date: 04-01-2020
# desc: convert a sorted array to height balanced BST

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def mini_BST(nums):

    if len(nums) == 0:
        return None

    mid = int(len(nums)/2)

    root = TreeNode(nums[mid])

    root.left = mini_BST(nums[:mid])
    root.right = mini_BST(nums[mid+1:])

    return root

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
       root = mini_BST(nums)

 
if __name__ == '__main__':
    list_nums = [-10, -3, 0, 5, 9]

    Solution().sortedArrayToBST(list_nums)