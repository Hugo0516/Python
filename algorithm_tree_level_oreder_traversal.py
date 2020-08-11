# Recursive Python program for level order traversal of Binary Tree

# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Function to print level order traversal of tree
def printLevelOrder(root):
    h = height(root)
    for i in range(1, h + 1):
        printGivenLevel(root, i)


# Print nodes at a given level
def printGivenLevel(root, level):
    if root is None:
        return
    if level == 1:
        print(root.data, end=" ")
    elif level > 1:
        printGivenLevel(root.left, level - 1)
        printGivenLevel(root.right, level - 1)


""" 
    Compute the height of a tree--the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""


def height(node):
    if node is None:
        return 0
    else:
        # Compute the height of each subtree
        lheight = height(node.left)
        rheight = height(node.right)

        # Use the larger one
        if lheight > rheight:
            return lheight + 1
        else:
            return rheight + 1


# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level order traversal of binary tree is -")
printLevelOrder(root)
print('\n')

"""
    不管是以疊代或是遞迴的方式，前序 中序 後序，都需要用到一個堆疊，
    level-order traversal 是用 queue 的走訪方式
    Level-order traversal 就是和 BFS 差不多的思維方式 
    
    
    這裡呈現兩種方式，看需求是啥 (這上面是用 function to print a given level)
    Time Complexity: O(n^2) in worst case. For a skewed tree,
    printGivenLevel() takes O(n) time where n is the number of nodes in the skewed tree.
    So time complexity of printLevelOrder() is O(n) + O(n-1) + O(n-2) + .. + O(1) which is O(n^2).
    
    Space Complexity: O(n) in worst case. For a skewed tree,
    printGivenLevel() uses O(n) space for call stack. 
    For a Balanced tree, call stack uses O(log n) space, (i.e., height of the balanced tree).
    
    height function 可能得看一下，沒看很了解
    
    
"""


# Python program to print level order traversal using Queue

# A node structure
class Node:
    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


# Iterative Method to print the height of a binary tree
def printLevelOrder2(root):
    # Base Case
    if root is None:
        return

    # Create an empty queue for level order traversal
    queue = []

    # Enqueue Root and initialize height
    queue.append(root)

    while queue:
        # Print front of queue and remove it from queue
        print(queue[0].data, end=' ')
        node = queue.pop(0)

        # Enqueue left child
        if node.left is not None:
            queue.append(node.left)

        # Enqueue right child
        if node.right is not None:
            queue.append(node.right)


# Driver Program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Level Order Traversal of binary tree is -")
printLevelOrder2(root)

"""
    pre-order, in-order, post-order traversal 都是 DFS 的應用
    level-order traversal 是 BFS 的應用
    記最後一個版本！！！！！！！！
    
    我覺得 queue 的方法比較簡單 !!!!!!!!!
    c 課本是說用circular queue 啦， 但這個版本沒有用 circular
    Time Complexity: O(n) where n is number of nodes in the binary tree
    
    level-order traversal 的 space complexity 和其他 traversal 很不一樣
    Space Complexity: O(n) where n is number of nodes in the binary tree
    Worst-Case (when the tree is balanced): O(n)

    When the tree is balanced, the last level will have the maximum number of nodes and that will be 2^h. And for a balanced tree, 
    h will be log n. So O(2^h) => O(2 ^ (log n)) => O(n)
    
    Best-Case (when the tree is a degenerate linked list): O(1)
    When the tree is a degenerated linked list, every level will have a maximum of one node and thus at any point of time, 
    there will be at most one node in the queue.

    https://stackoverflow.com/questions/17635950/space-complexity-of-level-order-traversal-traversal-using-a-queue
    https://www.geeksforgeeks.org/level-order-tree-traversal/?ref=lbp
"""
