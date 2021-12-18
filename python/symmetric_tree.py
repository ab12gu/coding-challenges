##
# 
# filename: symmetric_tree.py
# by: Abhay Gupta
# date: 03-28-20
#
# desc: given a binary tree, check if it is a mirror of itself (symmetric around center)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def symmetric(left, right):
    if (left == None and right == None): 
        return True
    if (left == None or right == None): 
        return False
    if left.val != right.val:
        return False
    else:
        return symmetric(left.left, right.right) and symmetric(left.right, right.left)

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None:
            return True
        # return symmetric(root.left, root.right)
    
        queue = []
        queue.append(root)
        queue.append(root)
        while(len(queue) > 0):
            
            v1 = queue.pop(0)
            v2 = queue.pop(0)

            if v1 == None and v2 == None:
                continue
            if v1 == None or v2 == None:
                return False
            if v1.val != v2.val:
                return False
            
            queue.append(v1.right)
            queue.append(v2.left)
            queue.append(v1.left)
            queue.append(v2.right)
            
        return True
            