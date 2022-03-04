# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None or sum is None:
            return False
        
        queue = []
        queue.append(root)
        queue.append(sum)
        
        while len(queue) > 0:
            
            root = queue.pop(0)
            val = queue.pop(0)
            
            val -= root.val
            
            if root.left is None and root.right is None:
                if val == 0:
                    return True
                continue
                
            if root.left is not None:
                queue.append(root.left)
                queue.append(val)
            if root.right is not None:
                queue.append(root.right)
                queue.append(val)
        
        return False
                