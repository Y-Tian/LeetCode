# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        stack = []
        while root is not None:
            stack.append(root)
            root = root.left
            while root is None:
                if len(stack) == 0:
                    return result
                root = stack.pop()
                result.append(root.val)
                root = root.right
        return result