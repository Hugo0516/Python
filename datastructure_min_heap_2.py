class Heap:
    def __init__(self, size):
        self.maxsize = size
        self.front = 1
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = float("-inf")
        self.curr = 0

    def insert(self, element):
        if self.curr >= self.maxsize:
            return

        self.curr += 1
        self.heap[self.curr] = element
        tmp = self.curr
        parent = self.curr // 2

        while self.heap[tmp] < self.heap[parent]:
            self.heap[tmp], self.heap[parent] = self.heap[parent], self.heap[tmp]
            tmp = parent
            parent = tmp // 2

    def extract(self):
        if self.curr < 1:
            return
        item = self.heap[self.front]
        self.heap[self.front] = self.heap[self.curr]
        self.curr -= 1
        self.heapify(self.front)
        return item

    def heapify(self, start):
        if start >= self.curr:
            return

        left_child = start * 2
        right_child = start * 2 + 1
        temp = start

        if left_child < self.curr and self.heap[left_child] < self.heap[temp]:
            temp = left_child

        if right_child < self.curr and self.heap[right_child] < self.heap[temp]:
            temp = right_child

        if temp != start:
            self.heap[temp], self.heap[start] = self.heap[start], self.heap[temp]
            self.heapify(temp)


if __name__ == '__main__':
    min_heap = Heap(15)
    min_heap.insert(5)
    min_heap.insert(3)
    min_heap.insert(17)
    min_heap.insert(10)
    min_heap.insert(84)
    min_heap.insert(19)
    min_heap.insert(6)
    min_heap.insert(22)
    min_heap.insert(9)

    for i in range(1, min_heap.curr + 1):
        print(min_heap.heap[i], end=' ')
    print('\n')
    min_heap.extract()
    for i in range(1, min_heap.curr + 1):
        print(min_heap.heap[i], end=' ')
