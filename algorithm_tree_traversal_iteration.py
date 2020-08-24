# Python program to do inorder traversal without recursion
# A binary tree node
class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


# Iterative function to perform in-order traversal of the tree
def inorderIterative(root):
    # Base CAse
    if root is None:
        return
    # create an empty stack
    stack = []
    # start from root node (set current node to root node)
    # curr = root

    # if current node is None and stack is also empty, we're done
    while stack or root:  # 這裏底下的 root 原本是 curr (19 行)
        # if current node is not None, push it to the stack (defer it)
        # and move to its left child
        if root:
            stack.append(root)
            root = root.left
        else:
            # else if current node is None, we pop an element from the stack,
            # print it and finally set current node to its right child
            root = stack.pop()
            print(root.data, end=' ')
            root = root.right


# Driver program to test above function
""" 
Constructed binary tree is 
		 1 
		/ \ 
	   2   3 
	  / \ 
     4   5 
        / \
       6   7
            \
              8
     
     4->2->5->1->3
"""

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.left.right.left = Node(6)
root.left.right.right = Node(7)
root.left.right.right.right = Node(8)

inorderIterative(root)
print()


# Python program to perform iterative preorder traversal
# An iterative process to print preorder traveral of BT
def Preorderiterative(root):
    # Base CAse
    if root is None:
        return

    # create an empty stack and push root to it
    nodeStack = []
    nodeStack.append(root)

    # Pop all items one by one. Do following for every popped item
    # a) print it
    # b) push its right child
    # c) push its left child
    # Note that right child is pushed first so that left
    # is processed first */
    while nodeStack:

        # Pop the top item from stack and print it
        node = nodeStack.pop()
        print(node.data, end=' ')

        # Push right and left children of the popped node
        # to stack
        if node.right:
            nodeStack.append(node.right)
        if node.left:
            nodeStack.append(node.left)

        # Driver program to test above function


"""
        10
       /  \
      8    2
     / \  /
    3   5 4
    10->8->3->5->2->4
"""

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(4)
Preorderiterative(root)
print()


# Iterative function to perform post-order traversal of the tree
def postorderIterative(root):
    if root is None:
        return
    # create an empty stack and push root node
    stack = []
    stack.append(root)
    # create another stack to store post-order traversal
    out = []

    # run till stack is not empty
    while stack:
        # we pop a node from the stack and push the data to output stack
        curr = stack.pop()
        out.append(curr.data)

        # push left and right child of popped node to the stack
        if curr.left:
            stack.append(curr.left)

        if curr.right:
            stack.append(curr.right)
    # print post-order traversal
    while out:
        print(out.pop(), end=' ')


"""
        10
       /  \
      8    2
     / \  /
    3   5 4
    3->5->8->4->2->10
"""

root = Node(10)
root.left = Node(8)
root.right = Node(2)
root.left.left = Node(3)
root.left.right = Node(5)
root.right.left = Node(4)
postorderIterative(root)

"""
    The time complexity of above method solutions is O(n), and space complexity of the program is O(n) as space
    proportionate to the height of the tree which can be equal to number of nodes in the tree in worst case for skew tree.
    
    所以說， space complexity worst:O(n) (skewed tree), best: O(LogN)==O(height) (balanced tree)
    
    post-oder 的 space complexity = O(n) 因為 有一個out 儲存所有node
    
    https://www.techiedelight.com/inorder-tree-traversal-iterative-recursive/
    https://www.techiedelight.com/postorder-tree-traversal-iterative-recursive/
    https://www.techiedelight.com/preorder-tree-traversal-iterative-recursive/
"""
