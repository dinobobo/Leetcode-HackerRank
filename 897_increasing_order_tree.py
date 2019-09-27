# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def increasingBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """       
        self.cur = TreeNode(None)
        ans = self.cur
        self.inorder(root)
        return ans.right
        
        
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            root.left = None
            self.cur.right = root
            self.cur = root
            self.inorder(root.right)