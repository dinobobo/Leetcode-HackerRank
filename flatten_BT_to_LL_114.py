# class Solution:
#     def flatten(self, root: TreeNode) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         def sub_flatten(node):
#             if node.left == None and node.right == None:
#                 return (node, node)
#             l_node, r_node = node.left, node.right
#             if l_node != None:
#                 head_l, tail_l = sub_flatten(l_node)
#                 node.right = head_l
#                 node.left = None
#             else:
#                 head_l = node
#                 tail_l = node
            
            
#             if r_node != None:
#                 head_r, tail_r = sub_flatten(r_node)
#                 tail_l.right = head_r
#             else:
#                 tail_r = tail_l
#             return (node, tail_r)
        
        
#         if root == None:
#             return None
        
#         return sub_flatten(root)[0] 
        