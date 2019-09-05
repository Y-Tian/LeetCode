# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        hashmap = {}
        index = 0
        curr = head
        while curr is not None:
            # no cycle case
            if curr.next is None:
                return None
            if curr.next in hashmap:
                return curr.next
            hashmap[curr] = index
            curr = curr.next
            index = index + 1
            
        return None
        