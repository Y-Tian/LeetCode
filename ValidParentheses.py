class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Brute force:
        # Turn string to array
        # Has to be an even length as well
        # Empty string is valid
        
        stack = []
        s_temp = list(s)
        if len(s_temp) == 0:
            return True
        if len(s_temp)%2 == 1:
            return False
        
        for c in s_temp:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            elif c == ')':
                if len(stack) == 0:
                    return False
                if stack.pop() != '(':
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                if stack.pop() != '{':
                    return False
            elif c == ']':
                if len(stack) == 0:
                    return False
                if stack.pop() != '[':
                    return False
        
        
        
        return len(stack) == 0