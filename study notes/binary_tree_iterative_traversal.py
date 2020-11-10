#Binary tree traversal inorder, preorder, and postorder with iterative approach. 

class tree_node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None



#In order iterative left -> root -> right
def inorder_it(node):
    if node == None:
        return None

    node_st = []
    while len(node_st) != 0 or node != None:
        while node != None:
            # Visit all the left nodes, obviously you don't want to add the root node
            # None node should be excluded too
            node_st.append(node)
            node = node.left

        node = node_st.pop() # Pop the most left node
        print(node.val)
        
        # We want the right node to be visited too
        node = node.right


def inorder_it_2(node):
    node_st = []
    while True:
        if node != None: # Exhaust all the left nodes DFS
            node_st.append(node)
            node = node.left

        elif len(node_st) != 0: 
            #Once the all the left nodes and current nodes are done
            #Go visit the right node, and this basically is a recursive call
            node = node_st.pop()
            print(node.val)
            node = node.right

        else:
            break



#Pre order iterative root -> left -> right
def preorder_it(node):
    node_st = []
    node_st.append(node)

    while len(node_st) != 0:
        node = node_st.pop()
        print(node.val)
        if node.right:
            node_st.append(node.right)
        if node.left:
            node_st.append(node.left)

        

#Post order iterative right -> left -> root
def postorder_it_2st(node):
    # The idea is that the order of nodes in the stack is similar to the stack
    # established for a preorder traversal. The INVERSE of the postorder stack
    # is the same as the preorder stack, BUT goes as root -> right -> left.
    # Isn't it obvious if you look at the ordering?
    st_temp = []
    st_post = []
    st_temp.append(node)
    while len(st_temp) != 0:
        node = st_temp.pop()
        st_post.append(node)
        if node.left:
            st_temp.append(node.left)
        if node.right:
            st_temp.append(node.right)
    for i in st_post[::-1]:
        print(i.val)



def postorder_it_1st(node):
    # The key here is that you push the right child THEN the root into the stack
    # Upon visiting a node with a right child, and this child happens to be on 
    # the top of the stack, this node has to be visited.
    node_st = []

    while len(node_st) != 0 or node != None:
        while node != None:
            if node.right != None:
                node_st.append(node.right)
            node_st.append(node)
            node = node.left

        node = node_st.pop()
        if node.right != None and len(node_st) > 0 and node_st[-1] == node.right:
            node_st.pop()
            node_st.append(node)
            node = node.right
        else:
            print(node.val)
            node = None # Set it to None so that it won't be revisited.





#Test
root = tree_node(3)
first_left = tree_node(5)
first_right = tree_node(1)
root.left = first_left
root.right = first_right
first_left.left = tree_node(10)
first_left.right = tree_node(4)
first_right.left = tree_node(0)
first_right.right = tree_node(14)

inorder_it(root)
inorder_it_2(root)
preorder_it(root)
postorder_it_2st(root)
postorder_it_1st(root)

