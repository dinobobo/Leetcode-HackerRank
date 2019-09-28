from collections import deque
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        ans = []
        if root:
            tq = deque([[root]])
            while tq:
                nodes = tq.popleft()
                next_nodes = []
                ans.append([j.val for j in nodes])
                for i in nodes:
                    next_nodes += i.children
                if next_nodes:
                    tq.append(next_nodes)
        return ans