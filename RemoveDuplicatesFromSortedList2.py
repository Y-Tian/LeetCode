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
        # Have to keep track of current node + consecutive nodes
        # We can create a stack to keep track of consecutive nodes
        # Run a single pass on the linked list
        # For every node, we can store the node in a stack
        # If the next node isn't the same, we can pop it and link it to our result list
        # We make the comparison by doing a peek at the stack
        
        stack = []
        curr = head
        result = temp = ListNode(0)
        
        
        # we want to begin with a reference value in the stack, so start at index 1
        if curr is not None:
            # edge case of only 1 node
            if curr.next is None:
                result.next = ListNode(curr.val)
            
            stack.append(curr.val)
            
            curr = curr.next
        
            while curr is not None:
                # store & ignore duplicates
                if stack.count(curr.val) != 0:
                    stack.append(curr.val)
                else:
                    # if no duplicate, store in the result linked list
                    if len(stack) == 1:
                        v = stack.pop()
                        temp.next = ListNode(v)
                        temp = temp.next
                    # check the tail node
                    if curr.next is None:
                        temp.next = ListNode(curr.val)
                    stack = []
                    stack.append(curr.val)
                
                curr = curr.next
                
                
        return result.next
        