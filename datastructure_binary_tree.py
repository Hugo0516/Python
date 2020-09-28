class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        # Compare the new value with the parent node
        # 這裡的寫的分配方式跟 binary search tree 一樣，但是如果是 binary tree的話其實不用那麼嚴格
        if self.data:
            if data <= self.data:
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

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()



# Use the insert method to add nodes
root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(5)
root.insert(4)

root.PrintTree()
print()

"""
    we can also use array!!! to store binary tree; however, as u know,
    if there are too many spare space inside the tree, we would waste lost of space to store empty thing
    !!!! if the tree is complete binary tree, then array is a good way to implement it!!!!
    
    Therefore, linked-list is a better way to store binary tree
    
    Tree: skewed tree, binary tree, complete binary tree, full binary tree, binary search tree
    => in-order, pre-order, post-order
    
    還有一些題型：像是 copy 一顆tree 或是問說一個tree對不對襯之類的
    
    Tree is a undirected graph !!!
"""