##
# filename: level_order_bottom.py
#
# by: Abhay Gupta
# date: 04-01-2020
# desc: Given a binary tree, return the bottom-up level order transversal of its nodes' values

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root,):
    
    if root == None:
        return -1 
    return (max(maxDepth(root.left)+1, maxDepth(root.right)+1))
    

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:        
        
        max_length = maxDepth(root) + 1
        temp = []
        for i in range(max_length):
            temp.append([])
        
        
        queue = [root]
        max_length -= 1
        queue.append(max_length)
        
        while(len(queue)>0):
            root = queue.pop(0)
            length = queue.pop(0)
            
            if root == None:
                continue
                
            temp[length].append(root.val)
            
            length -= 1
            queue.append(root.left)
            queue.append(length)
            queue.append(root.right)
            queue.append(length)
            

        return temp

if __name__ == "__main__":
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)

    print( Solution().levelOrderBottom(root) ) 