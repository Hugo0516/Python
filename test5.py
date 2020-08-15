def heapify(array, length, start):
    if start >= length:
        return
    left_child = 2 * start + 1
    right_child = 2 * start + 2
    temp = start

    if left_child < length and array[left_child] > array[temp]:
        temp = left_child
    if right_child < length and array[right_child] > array[temp]:
        temp = right_child

    if temp != start:
        array[temp], array[start] = array[start], array[temp]
        heapify(array, length, temp)


def buildheap(array):
    length = len(array) - 1
    parent = (length - 1) // 2
    for i in range(parent, -1, -1):
        heapify(array, length, i)


def heapsort(array):
    length = len(array) - 1
    buildheap(array)
    for i in range(length, -1, -1):
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)


"""
    root 重 1 開始好惹
"""
array = [61, 52, 43, 34, 25, 16]
heapsort(array)
print(array)
