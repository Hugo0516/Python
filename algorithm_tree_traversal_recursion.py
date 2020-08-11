class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert Node
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    # Print the Tree
    # Fuck I think this method is same as inorderTraversal
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()

    # 這個格式感覺比上面的好？？？
    def print_tree2(self, root):
        if root:
            self.print_tree2(root.left)
            print(root.data)
            self.print_tree2(root.right)

    # Inorder traversal
    # Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

    # 記這個解法!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    def inorder_traversal2(self, root, res):
        if root:
            self.inorder_traversal2(root.left, res)
            res.append(root.data)
            self.inorder_traversal2(root.right, res)


    # Preorder traversal
    # Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

    # Postorder traversal
    # Left -> Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res


# 這樣寫就不用跟上面一樣麻煩惹
def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.data)
        print_tree(root.right)


root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
root.PrintTree()
print()
root.print_tree2(root)
print()
print_tree(root)
print()
res = []
root.inorder_traversal2(root, res)
print(res)

print(root.inorderTraversal(root))

print(root.PreorderTraversal(root))

print(root.PostorderTraversal(root))

"""
    Traversal is a process to visit all the nodes of a tree and may print their values too. 
    Because, all nodes are connected via edges (links) we always start from the root (head) node.
    That is, we cannot randomly access a node in a tree. There are three ways which we use to traverse a tree −
    In-order Traversal / Pre-order Traversal / Post-order Traversal
    
    Traversal 是 binary tree 的 related-problem
    我們這裡的 traversal 都是用 recursion 來表示，但是也都可以改成iteration method,
    我們知道 recursion 會用到 stack frame; therefore, if we want to implement iteration method,
    we need to simulate a stack => which means, simulate stack + iteration = recursion
    
    =>> no matter recursion or iteration edition of traversal, we both need to have a stack; however,
    now, we can abandon stack replaced by queue method.(用 環狀佇列)
    which is called level-order traversal
    
    (PS. DFS like pre-order traversal, BFS like lever-order traversal)
    
    上面所有做法的 Time Complexity: O(n) (也可以用圖來想 graph: O(n+m) m = n-1(edge的個數) = O(n)
    / Space Complexity: worst:O(n)(例如: skewed tree) best:O(logN)(balanced tree) 其實也可以寫O(height)
    因為每個點都一定要走訪，所以Time 一定是O(n) / space 和樹深成正比, so max:O(n) / best:O(LogN)
    If we don’t consider size of stack for function calls then O(1) otherwise O(n).
    
    In-order, Pre-order, and Post-order traversals are Depth-First traversals.
    For a Graph, the complexity of a Depth First Traversal is O(n + m), where n is the number of nodes, and m is the number of edges.
    Since a Binary Tree is also a Graph, the same applies here. The complexity of each of these Depth-first traversals is O(n+m).
    Since the number of edges that can originate from a node is limited to 2 in the case of a Binary Tree,
    the maximum number of total edges in a Binary Tree is n-1, where n is the total number of nodes.
    The complexity then becomes O(n + n-1), which is O(n).
    
    
    https://stackoverflow.com/questions/4547012/complexities-of-binary-tree-traversals
    https://www.tutorialspoint.com/python_data_structure/python_tree_traversal_algorithms.htm
"""
