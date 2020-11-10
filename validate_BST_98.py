class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     def isValidBST(self, root):
#         return self.valid_limits(root, -float('inf'), float('inf'))
        
        
#     def valid_limits(self, root, lower, upper):
#         if root == None:
#             return True
#         if root.val <= lower or root.val >= upper:
#             return False
#         return self.valid_limits(root.right, root.val, upper) and self.valid_limits(root.left, lower, root.val)

# Iterative approach
# class Solution:
#      def isValidBST(self, root):
#             if root == None:
#                 return True
#             node_arr = []
#             lower, upper = -float('inf'), float('inf')
#             node_arr.append((root, lower, upper))
#             while node_arr != []:
#                 node, lower, upper = node_arr.pop(-1)
#                 if node.val <= lower or node.val >= upper:
#                     return False
#                 if node.left:
#                     node_arr.append((node.left, lower, node.val))
#                 if node.right:
#                     node_arr.append((node.right, node.val, upper))
#             return True

# In order traversal
class Solution:
     def isValidBST(self, root: TreeNode) -> bool:
            stack = []
            node = root
            prev = -float('inf')
            while stack or node:
                while node != None:
                    stack.append(node)
                    node = node.left
                node = stack.pop()
                if node != None:
                    if node.val <= prev:
                        return False
                    prev = node.val
                node = node.right
            return True



ans = Solution()
root = Node(5)
l = Node(1)
r = Node(4)
r.left = Node(3)
r.right = Node(6)
root.left = l
root.right = r


#Test:
ans.valid_min(root.right)
ans.valid_max(root.right)
