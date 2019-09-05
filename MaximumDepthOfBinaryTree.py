# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        depth = 0
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1
        left_temp = self.maxDepth(root.left)
        right_temp = self.maxDepth(root.right)
        if left_temp > right_temp:
            return 1 + left_temp
        else:
            return 1 + right_temp