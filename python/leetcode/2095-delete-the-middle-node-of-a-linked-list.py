# filename: middle node pop linked list
#
# Abhay Gupta

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def print(head):
        while head is not None:
            print(head.val)
            head = head.next

class Solution:
    def deleteMiddle(self, head):
        first = head
        center = head
        count = 0

        while head is not None:
            count = count + 1
            head = head.next

        if count == 2:
            first.next = None
            return first

        for i in range(int(count/2)):
            center = center.next

        center.val = center.next.val
        center.next = center.next.next

        return first
       
head = [1,3,4,7,1,2,6]
node = ListNode(head.pop())

for i in range(len(head)):
    node = ListNode(head[-i-1], node)

#ListNode.print(node)

solution = Solution()
solution.deleteMiddle(node)

ListNode.print(node)


