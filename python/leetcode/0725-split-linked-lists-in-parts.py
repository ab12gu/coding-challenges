# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:

        arr = [] 
        while(head):
            arr.append(head)
            head = head.next

        split = len(arr) // k
        remainder = len(arr) % k

        output = [None] * k
        r = 0
        for i in range(min(len(arr), k)):
            if i > 0:
                arr[i*split+r-1].next = None

            output[i] = arr[i*split+r]
            if i < remainder:
                r += 1

        return output
