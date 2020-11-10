# from collections import deque
# class Solution:
#     def connect(self, root: 'Node') -> 'Node':
#         if root == None:
#             return None
#         queue = deque([root])
#         while len(queue) != 0:
#             q_len = len(queue)
#             pre, now = None, None
#             for _ in range(q_len):
#                 if now != None:
#                     pre = now
#                 now = queue.popleft()
#                 if now.left:
#                     queue.append(now.left)
#                 if now.right:
#                     queue.append(now.right)
#                 if pre and now:
#                     pre.next = now
#         return root

#O(1) space solution
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        left_most = root
        while left_most.left:
            node = left_most
            while node:
                node.left.next = node.right
                if node.next:
                    node.right.next = node.next.left
                node = node.next
            left_most = left_most.left
        return root