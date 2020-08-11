# 假設最大堆積大小

class MaxHeap:

    def __init__(self, max_size):
        self.maxsize = max_size
        self.heap = [0] * (self.maxsize + 1)  # +1, 因為想要讓頭從1開始
        self.size = 0

    def push(self, item):
        if self.size >= self.maxsize:
            print("It is full")
            return

        self.size += 1
        current = self.size
        while current != 1 and item > self.heap[current // 2]:
            self.heap[current] = self.heap[current // 2]
            current //= 2

        self.heap[current] = item

    def pop(self):
        if self.size == 0:
            print("It is empty")
            return
        item = self.heap[1]
        temp = self.heap[self.maxsize]
        parent, child = 1, 2
        while child <= self.maxsize:
            # 從目前的父節點，找最大的孩子
            if child < self.maxsize and self.heap[child] < self.heap[child + 1]:
                child += 1
            if temp >= self.heap[child]:
                break
            # 移到下一層
            self.heap[parent] = self.heap[child]
            parent = child
            child *= 2

        self.heap[parent] = temp
        print("pop out {}".format(item))


if __name__ == '__main__':
    demo = MaxHeap(15)
    demo.push(14)
    demo.push(10)
    demo.push(15)
    demo.push(2)
    demo.push(20)
    # demo.push(21)
    for i in range(1, 15):
        if demo.heap[i] == 0:
            break
        else:
            print(demo.heap[i], end=' ')

    print("\n")

    demo.pop()
    print(demo.heap[1], demo.heap[2], demo.heap[3], demo.heap[4], demo.heap[5])
    demo.pop()
    print(demo.heap[1], demo.heap[2], demo.heap[3], demo.heap[4], demo.heap[5])
    demo.pop()
    print(demo.heap[1], demo.heap[2], demo.heap[3])
