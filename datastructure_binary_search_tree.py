class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

    # Insert method to create nodes
    def insert(self, data):
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

    def remove(self, pre, data):
        if self is None:
            return None
        else:
            if data < self.data:
                if self.left is None:
                    return None
                else:
                    self.left.remove(self, data)

            elif data > self.data:
                if self.right is None:
                    return None
                else:
                    self.right.remove(self, data)

            elif self.left and self.right is not None:
                pre, tmp = self, self.right
                while tmp.left:
                    pre, tmp = tmp, tmp.left
                if tmp is self.right:
                    self.data = tmp.data
                    self.right = None
                else:
                    self.data = tmp.data
                    pre.left = None

            elif self.left and self.right is None:
                if pre.left is self:
                    pre.left = None
                elif pre.right is self:
                    pre.right = None
            else:
                if self.left is None:
                    pre, tmp = self, self.right
                    while tmp.left:
                        pre, tmp = tmp, tmp.left
                    if tmp is self.right:
                        self.data = tmp.data
                        self.right = None
                    else:
                        self.data = tmp.data
                        pre.left = None
                else:
                    pre, tmp = self, self.left
                    while tmp.right:
                        pre, tmp = tmp, tmp.right

                    if tmp is self.left:
                        self.data = tmp.data
                        self.left = None
                    else:
                        self.data = tmp.data
                        pre.right = None



    # findval method to compare the value with nodes
    def findval(self, lkpval):
        if self.data is None:
            return None
        if lkpval == self.data:
            return str(self.data) + ' is found'
        if lkpval < self.data:
            if self.left is None:
                return 'cant find'
            else:
                return self.left.findval(lkpval)
        if lkpval > self.data:
            if self.right is None:
                return "cant find"
            else:
                return self.right.findval(lkpval)

    # iteration version search:
    def iter_search(self, value):
        while self:
            if value == self.data:
                return str(self.data) + " is found"
            if value < self.data:
                self = self.left
            else:
                self = self.right
        return None

    # Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(12)

print(root.findval(7))
print(root.findval(14))
print(root.iter_search(3))
print('\n')

root.PrintTree()

root2 = Node(None)
root2.iter_search(11)


"""
    Binary search tree, 不一定是 complete binary tree 哦
    h 可能為 LogN or N (N 為 node 個數) 
    (我們可以說平均高度是 LogN ，因為此樹是 balanced的)
    (但是當此數不balanced，像是全部都在左邊 or 右邊，這時高度就變成 N 了)
    Thus, average = LogN, worst = N

    https://stackoverflow.com/questions/14426790/why-lookup-in-a-binary-search-tree-is-ologn    
    
    search an element: Time Complexity: O(h) (h為高度)
    insert an element: Time Complexity: O(h) (因為要先搜尋，後插入(插入就是O(1)) (所以 O(h) + O(1) = O(h))
    
    Tree is a undirected graph !!!
    
    iteration version 要看一下
    然後，我曾想說 35, 40 不要加 return, 可是後來發現會錯， 因為就算30找到值 return 要跑回來
    可是35, 40 沒寫return 那就直接胎死腹中
    

"""
