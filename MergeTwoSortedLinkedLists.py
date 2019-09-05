# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = head = ListNode(0)
        while(l1 is not None and l2 is not None):
            temp = ListNode(0)
            if l1.val <= l2.val:
                temp.val = l1.val
                # pop head
                l1 = l1.next
            else:
                temp.val = l2.val
                # pop head
                l2 = l2.next
            head.next = temp
            head = head.next
        
        if l1 is not None:
            head.next = l1
        else:
            head.next = l2
        
        return result.next

            
        