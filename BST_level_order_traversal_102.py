class Solution:
    def levelOrder(self, root):
        st = []
        ans = []
        node = root
        st.append([node, 0])
        while len(st) != 0:
            node, lvl = st.pop()
            if len(ans) < lvl + 1 and node != None:
                ans.append([])
            if node != None:
                ans[lvl].append(node.val) # Load node value into the answer
            
            # Add nodes from right to left so that they will be in order in the ans
            lvl += 1
            if node != None:
                st.append([node.right, lvl])
                st.append([node.left, lvl])
        return ans
