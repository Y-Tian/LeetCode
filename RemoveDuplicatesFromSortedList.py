# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Brute force:
        # create a hashmap with value as true if inserted
        hashmap = {}
        curr = head
        result = temp = ListNode(0)
        
        while curr is not None:
            if curr.val not in hashmap:
                hashmap[curr.val] = True
                temp.next = ListNode(curr.val)
                temp = temp.next
            curr = curr.next
            
        return result.next
        