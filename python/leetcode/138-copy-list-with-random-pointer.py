"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        # add lookup table of input index's
        arr_dict = {}

        arr = []
        c = 0

        while(head):
            arr.append(head)
            arr_dict[head] = c
            head = head.next 
            c += 1

        next_node = None
        size = len(arr)
        output_arr = [0] * size

        for c in range(size):
            head = Node(arr[-(c+1)].val, next_node)
            output_arr[-(c+1)] = head
            next_node = head

        for i in range(size):
            if arr[i].random:
                next_node.random = output_arr[arr_dict[arr[i].random]]
            next_node = next_node.next

        return head
       
