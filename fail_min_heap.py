import sys
class MinHeap:
    def __init__(self, max_size):
        self.maxsize = max_size
        self.heap = [-sys.maxsize] * (self.maxsize + 1)
        self.size = 0

    def push(self, item):
        if self.size >= self.maxsize:
            print("It is full")
            return
        self.size += 1
        current = self.size

        while current != 1 and item < self.heap[current//2]:
            self.heap[current] = self.heap[current//2]
            current //= 2

        self.heap[current] = item


if __name__ == '__main__':
    demo = MinHeap(15)
    demo.push(5)
    demo.push(4)
    demo.push(3)
    demo.push(2)
    demo.push(1)

    for i in range(1, 15):
        if demo.heap[i] == -sys.maxsize:
            break
        else:
            print(demo.heap[i], end=' ')