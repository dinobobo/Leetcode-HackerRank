# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        return self.leaf_val(root1) == self.leaf_val(root2)
    def leaf_val(self, root):
        ans = []
        if root:
            val_l = self.leaf_val(root.left)
            if not root.left and not root.right:
                ans.append(root.val)
            val_r = self.leaf_val(root.right)
            ans = val_l + ans + val_r
        return ans