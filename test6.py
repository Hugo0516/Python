class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def insert(self, data):
        new_node = Node(data)
        temp = self

        while temp.next:
            temp = temp.next
        temp.next = new_node

    def insert2(self, data):
        new_node = Node(data)
        while self.next:
            self = self.next
        self.next = new_node

def think(a, b):
    a = b+3
    b = b -1

if __name__ == '__main__':
    root = Node(0)
    root.insert(1)
    print(root)
    root.insert(2)
    print(root)
    root.insert(3)
    print(root)

    print(root.val, root.next.val, root.next.next.val, root.next.next.next.val)

    root2 = Node(1)
    root2.insert2(2)
    print(id(root2))
    root2.insert2(3)
    print(id(root2))
    root2.insert2(4)
    print(id(root2))

    print(root2.val, root2.next.val, root2.next.next.val, root2.next.next.next.val)

    x = 30
    y = 20
    think(x, y)
    print(x, y)