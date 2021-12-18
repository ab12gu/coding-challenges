##
#
# filename: is_balanced.py
#
# by: Abhay Gupta
# date: 04-02-2020
# desc: Given a binary tree, determine if it is height-balanced.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        if root is None:
            return True
    
        queue = []
        
        queue.append(root)
        queue.append(1)
        height = []
        
        while len(queue) > 0:
            root = queue.pop(0)
            length = queue.pop(0)
            
            if root.left is None or root.right is None:
                height.append(length)
                
            if root.right is not None:
                queue.append(root.right)
                queue.append(length + 1)
            if root.left is not None:
                queue.append(root.left)
                queue.append(length + 1)
       
        print(height)
        if max(height) - min(height) > 1:
            return False
        else:
            return True