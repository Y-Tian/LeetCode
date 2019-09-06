# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 7, 10, 7
        # 7, 
        # Case: carry over
        # Create a queue
        # Take the head and %10 to get the ones position
        # Check if a carry over is needed, we /10 and check for > 0 with math.floor()
        # Have a carry over flag
        
        queue = []
        curr1 = l1
        curr2 = l2
        result = temp = ListNode(0)
        
        # add and throw into a queue
        while curr1 is not None or curr2 is not None:
            if curr1 is not None and curr2 is not None:
                queue.append(curr1.val + curr2.val)
                curr1 = curr1.next
                curr2 = curr2.next
            elif curr1 is not None:
                queue.append(curr1.val)
                curr1 = curr1.next
            else:
                queue.append(curr2.val)
                curr2 = curr2.next
                
        carry = False
        for i in queue:
            carry_check = math.floor(i/10)
            ones = i%10
            if carry:
                ones = ones + 1
                if i+1 >= 10:
                    ones = ones%10
                else:
                    carry = False
            if carry_check > 0:
                carry = True
            temp.next = ListNode(ones)
            temp = temp.next
            
        if carry:
            temp.next = ListNode(1)
            temp = temp.next
        
        return result.next

        
        