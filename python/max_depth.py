##
# filename: max_depth.py
#
# by: Abhay Gupta
# date: 04-01-2020
# desc: given a binary tree, find maximum depth

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def maxDepth(root):
        if root == None:
            return -1
        else:
            return (max(maxDepth(root.right)+1, maxDepth(root.left)+1))

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return maxDepth(root) + 1

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    print( Solution().maxDepth(root) )