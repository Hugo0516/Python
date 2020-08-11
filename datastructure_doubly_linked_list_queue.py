# doubly linked-list edition
class Node2:

    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.prev = None  # Initialize prev as null


# Queue class contains a Node object
class Queue3:

    # Function to initialize head
    def __init__(self):
        self.head = None
        self.last = None

    # Function to add an element data in the Queue
    def enqueue(self, data):
        if self.last is None:
            self.head = Node2(data)
            self.last = self.head
        else:
            self.last.next = Node2(data)
            self.last.next.prev = self.last
            self.last = self.last.next

    # Function to remove first element and return the element from the queue
    def dequeue(self):

        if self.head is None:
            return None
        else:
            temp = self.head.data
            self.head = self.head.next
            self.head.prev = None
            return temp

        # Function to return top element in the queue

    def first(self):

        return self.head.data

    # Function to return the size of the queue
    def size(self):

        temp = self.head
        count = 0
        while temp is not None:
            count = count + 1
            temp = temp.next
        return count

    # Function to check if the queue is empty or not
    def isEmpty(self):

        if self.head is None:
            return True
        else:
            return False

    # Function to print the stack
    def printqueue(self):

        print("queue elements are:")
        temp = self.head
        while temp is not None:
            print(temp.data, end="->")
            temp = temp.next


# Code execution starts here
if __name__ == '__main__':
    # Start with the empty queue
    queue = Queue3()

    print("Queue operations using doubly linked list")

    # Insert 4 at the end. So queue becomes 4->None
    queue.enqueue(4)

    # Insert 5 at the end. So queue becomes 4->5None
    queue.enqueue(5)

    # Insert 6 at the end. So queue becomes 4->5->6->None
    queue.enqueue(6)

    # Insert 7 at the end. So queue becomes 4->5->6->7->None
    queue.enqueue(7)

    # Print the queue
    queue.printqueue()

    # Print the first element
    print("\nfirst element is ", queue.first())

    # Print the queue size
    print("Size of the queue is ", queue.size())

    # remove the first element
    queue.dequeue()

    # remove the first element
    queue.dequeue()

    # first two elements are removed
    # Print the queue
    print("After applying dequeue() two times")
    queue.printqueue()

    # Print True if queue is empty else False
    print("\nqueue is empty:", queue.isEmpty())
