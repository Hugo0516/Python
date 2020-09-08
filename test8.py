class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def something(self):
        # test = self
        # test.next.data = 99
        self.next.data = 99

if __name__ == '__main__':
    root = Node(0)
    root.next = Node(1)
    root.next.next = Node(2)
    root.next.next.next = Node(3)
    root.next.next.next.next = Node(4)
    root.next.next.next.next.next = Node(5)

    tempp = root
    while tempp:
        print(tempp.data, end=' ')
        tempp = tempp.next

    root.something()
    print(" ")

    while root:
        print(root.data, end=' ')
        root = root.next