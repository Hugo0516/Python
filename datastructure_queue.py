class Queue:

    def __init__(self):
        self.queue = []

    def addtoq(self, dataval):
        # Insert method to add element
        if dataval not in self.queue:
            self.queue.insert(0, dataval)
            return True
        return False

    # Pop method to remove element
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in Queue!")


TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())
print('')

"""
    queue 可以用array 或是 linked-list 實作
    queue 有很多種：circular queue(改善queue的問題), priority queue(不遵守FIFO,而是看priority),
                  dequeue(double-ended queue)(兩端都可以置入或是取出
    應用時機：電腦作業系統中，不考慮工作優先權時，依進入系統的先後順序來處理
            系統工作排程，I/O 的 Buffer 上, BFS 追蹤？？
"""




