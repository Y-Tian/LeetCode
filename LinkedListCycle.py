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
        # brute force:
        # create a hashmap with key=node, value=index
        # do a single pass on the list
        # check if map contains node or not
        # store each node into the map, and set the value to index
        # when map contains node, compare map value with pos
        # O(n)
        
        # edge case:
        # when pos = -1, tail.next = None
        
        hashmap = {}
        curr = head
        index = 0
        while curr is not None:
            if curr in hashmap:
                # if hashmap.get(curr) == pos:
                return True
                # return False
            else:
                hashmap[curr] = index
            curr = curr.next
            index = index + 1
            
        return False