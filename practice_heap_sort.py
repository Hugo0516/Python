from typing import List


def heapify(tree: List, length: int, index: int):
    if index > length:
        return
    left = index * 2
    right = index * 2 + 1
    largest = index

    if left < length and tree[left] > tree[largest]:
        largest = left
    if right < length and tree[right] > tree[largest]:
        largest = right

    if largest != index:
        tree[largest], tree[index] = tree[index], tree[largest]
        heapify(tree, length, largest)


def build_heap(tree: List):
    length = len(tree)
    for i in range((length - 1) // 2, -1, -1):
        heapify(tree, length, i)


def heap_sort(tree):
    build_heap(tree)
    for i in range(len(tree) - 1, -1, -1):
        tree[i], tree[0] = tree[0], tree[i]
        heapify(tree, i, 0)


input_1 = [4, 2, 1, 7, 8, 9, 3, 14, 10, 16]
heap_sort(input_1)
print(input_1)
