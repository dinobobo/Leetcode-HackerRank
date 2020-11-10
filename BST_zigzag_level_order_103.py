class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        lvl = 0
        queue = [root]
        ans = []
        while len(queue) != 0:
            ans.append([])
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.pop(0)
                ans[lvl].append(node.val)
                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
            if lvl % 2 == 1:
                ans[lvl] = ans[lvl][::-1]
            lvl += 1
        return ans
                    