class Max_Heap:

    def __init__(self, size):
        self.maxsize = size
        self.curr = 0
        self.front = 1
        self.heap = [0] * (self.maxsize + 1)
        self.heap[0] = float("inf")

    def insert(self, element):
        if self.curr >= self.maxsize:
            return
        self.curr += 1
        self.heap[self.curr] = element

        curr = self.curr
        parent = curr // 2
        while self.heap[curr] > self.heap[parent]:  # O(LogN)
            self.heap[curr], self.heap[parent] = self.heap[parent], self.heap[curr]
            curr = parent
            parent = curr // 2

    def extract(self):
        if self.curr < 1:
            return
        item = self.heap[self.front]
        self.heap[self.front] = self.heap[self.curr]
        self.curr -= 1
        self.heapify(self.front)    # O(LogN)

        return item

    def heapify(self, start):
        if start >= self.curr:
            return

        left_child = start * 2
        right_child = start * 2 + 1
        temp = start

        if left_child < self.curr and self.heap[left_child] > self.heap[temp]:
            # self.heap[left_child], self.heap[self.front] = self.heap[self.front], self.heap[left_child]
            temp = left_child

        if right_child < self.curr and self.heap[right_child] > self.heap[temp]:
            # self.heap[right_child], self.heap[self.front] = self.heap[self.front], self.heap[right_child]
            temp = right_child

        if temp != start:
            self.heap[temp], self.heap[start] = self.heap[start], self.heap[temp]
            self.heapify(temp)

"""
    看這個版本就好,
    heap 重點：insert 要注意有沒有超過 array 的 maxsize
    extract 要注意把 root 拿掉後，會用最下面來補, 補完大小亂掉了, 所以要用 heapify 去重新恢復大小順序
    
    Both insert and extract : Time Complexity : O(LogN)
"""

if __name__ == "__main__":
    max_heap = Max_Heap(15)
    max_heap.insert(5)
    max_heap.insert(3)
    max_heap.insert(17)
    max_heap.insert(10)
    max_heap.insert(84)
    max_heap.insert(19)
    max_heap.insert(6)
    max_heap.insert(22)
    max_heap.insert(9)

    for i in range(1, max_heap.curr + 1):
        print(max_heap.heap[i], end=' ')
    print('\n')
    max_heap.extract()

    for i in range(1, max_heap.curr + 1):
        print(max_heap.heap[i], end=' ')
