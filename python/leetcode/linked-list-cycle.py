## filename: linked-list-cycle.py
#
# by: Abhay Gupta
# date: 22-03-02
#
# desc: given "head", the head of a linked list, determine if the linked list has a cycle in it
#

## Linked list class
class LinkNode:
    """ singly linked list """
    ## define constructor
    def __init__ (self, x):
        ## pass in self, current instance of the class
        self.val = x        # value of node
        self.next = None    # pointer to next node

class Solution:
    """ define solution """
    ## define constructor
    def __init__(self):
        self.head = None

    def pushFirst(self, new_data):
        new_node = LinkNode(new_data)
        new_node.next = self.head
        self.head = new_node
        print("Current Node: ", new_node.val)
        if new_node.next is not None:
            print(new_node.next.val)

    def pushLast(self, newNode):
        pass

    def hasCycle(self, head):
        nodeList = []

        while(1):
            if head is None or head.next is None:
                return False
            if head.next in nodeList:
                return True
            nodeList.append(head)
            head = head.next

    # def hasCycle(self, head):

if __name__ == "__main__":
    print("Hello World");

    head_list = [2, 3, 0, -4]
    pos = 1

    LinkedList = Solution()

    for i in reversed(head_list):
        LinkedList.pushFirst(i)

    head = LinkNode(2)
    head.next = LinkNode(3)
    head.next.next = LinkNode(0)
    head.next.next.next = LinkNode(-4)
    head.next.next.next.next = head.next

    print(Solution().hasCycle(head))

    #print(head)
    #print(head.next.val)
    #print(Solution(1).head)

