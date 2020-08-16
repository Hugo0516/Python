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


def quicksort(array, left, right):
    if left >= right:
        return None

    i = left
    j = right
    key = array[left]

    while i != j:


        while array[i] <= key and i < j:
            i += 1

        while array[j] > key and i < j:
            j -= 1

        if i < j:
            array[i], array[j] = array[j], array[i]

    array[left], array[i] = array[i], array[left]

    quicksort(array, left, i - 1)
    quicksort(array, i + 1, right)


"""
    root 重開始好惹
"""
array = [61, 52, 43, 34, 25, 16]
heapsort(array)
print(array)

array_2 = [61, 52, 43, 34, 25, 16]
quicksort(array_2, 0, 5)
print(array_2)

graph = [[] for i in range(3)]
print(graph)