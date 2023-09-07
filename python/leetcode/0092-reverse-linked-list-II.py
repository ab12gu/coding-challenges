# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        arr = []
        left -= 1
        right -= 1

        if left == right:
            return head

        while(head):
            arr.append(head)
            head = head.next

        if left > 0:
            arr[left - 1].next = arr[right]
            head = arr[0]
        else:
            head = arr[right]

        prev = arr[right]
        
        if left == 0:
            left_end = None
        else:
            left_end = left - 1

        
        for i in arr[right-1:left_end:-1]:
            prev.next = i
            prev = i

        if right < len(arr) - 1:
            arr[left].next = arr[right + 1]
        else:
            arr[left].next = None

        return head
        
