# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        count = Solution.search(root) + 1
            
        return count

    def search(root):
        left,right = 0,0
        if root.right:
            right = Solution.search(root.right) + 1
        if root.left:
            left = Solution.search(root.left) + 1
        return max(left,right
