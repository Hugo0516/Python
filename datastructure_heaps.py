import heapq

H = [21, 1, 45, 78, 3, 5]
# Use heapify to covert to a heap and rearrange the elements
heapq.heapify(H)
print(H)

# Add element
heapq.heappush(H, 8)
print(H)

# Remove element from the heap
heapq.heappop(H)
print(H)

# Replace an element
heapq.heapreplace(H, 6)
print(H)

"""
    Heap is a special tree structure!!!! in which each parent node is less than or equal to its child node.
    Then it is called a Min Heap. 
    If each parent node is greater than or equal to its child node then it is called a max heap.
    It is very useful to use min-heap or max-heap to implement priority queues !!!!! 
    where the queue item with higher weightage is given more priority in processing.
    
    max-heap or min-heap is complete binary tree
    => generally, the structure of tree is linked-list; however, we have library to implement heap automatically
    we don't need to create tree firsty by ourselves
    => A heap is created by using python’s inbuilt library named heapq. 
    This library has the relevant functions to carry out various operations on heap data structure.
    
    heap queue( heapq )  is priority queue
"""
