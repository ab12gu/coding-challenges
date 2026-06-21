# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        root = Solution.tree(nums)

        return root


    def tree(nums):
        if not nums:
            return

        length = len(nums)
        half = int(length/2)
        root = TreeNode(nums[half])

        if length == 1:
            print(nums)
            return root
        
        root.left = Solution.tree(nums[0:half])
        root.right = Solution.tree(nums[half+1:length])

        return root



            
