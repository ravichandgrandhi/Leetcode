# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None or head.next is None:
            return False
        p1 = head
        p2 = head.next
        while p1 is not p2:
            if p2 is None or p2.next is None:
                return False
            p1 = p1.next
            p2 = p2.next.next
        return True
        