# Program to reverse a doubly linked list

# A node of the doubly linked list
class Node:

    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Function reverse a Doubly Linked List
    def reverse(self):
        temp = None
        current = self.head

        # Swap next and prev for all nodes of
        # doubly linked list
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        # Before changing head, check for the cases like
        # empty list and list with only one node
        if temp is not None:
            self.head = temp.prev

        # Given a reference to the head of a list and an

    # 我自己寫的，我比較喜歡這版本，可以和singly linked list 比較
    def reverse2(self):
        prev = None
        current_node = self.head
        next_node = current_node.next

        while next_node:
            current_node.next = prev
            current_node.prev = next_node
            prev = current_node
            current_node = next_node
            next_node = current_node.next

        current_node.next = prev
        current_node.prev = None
        self.head = current_node

    # integer,inserts a new node on the front of list
    def push(self, new_data):

        # 1. Allocates node
        # 2. Put the data in it
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node

    def printList(self, node):
        while node is not None:
            print(node.data)
            node = node.next


# Driver program to test the above functions
dll = DoublyLinkedList()
dll.push(2)
dll.push(4)
dll.push(8)
dll.push(10)

print(dll.printList(dll.head))

print("")
# Reverse doubly linked list
dll.reverse2()

print(dll.printList(dll.head))
print("")

# 用來檢測是否prev next 有正確連接
tmp = dll.head
choose = lambda tmp: tmp.next.data if tmp.next else "QQ"
choose2 = lambda tmp:tmp.prev.data if tmp.prev else "WW"
while tmp:
    print(choose2(tmp), tmp.data, choose(tmp))
    tmp = tmp.next

"""
    要熟記 reverse 解法
"""