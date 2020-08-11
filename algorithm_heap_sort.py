def heapify2(array, length, index):
    if index >= length:
        return
    c1 = 2 * index + 1
    c2 = 2 * index + 2
    max = index
    if c1 < length and array[c1] > array[max]:
        max = c1
    if c2 < length and array[c2] > array[max]:
        max = c2
    if max != index:
        array[max], array[index] = array[index], array[max]
        heapify2(array, length, max)


def build_heap(array):
    last_node = len(array) - 1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify2(array, len(array)-1, i)    # 不確定這裡是 len(array) or len(array)-1


def heap_sort2(array):
    length = len(array)
    build_heap(array)

    for i in range(length - 1, -1, -1):
        array[i], array[0] = array[0], array[i]
        heapify2(array, i, 0)


input2 = [12, 11, 13, 5, 6, 7]
heap_sort2(input2)
print(input2)

"""
    注意這只是 complete binary tree 而已 不是 binary search tree!!!
    Time Complexity: Best and Worst: O(NLogN)
    Space Complexity: O(1) (As in-place method)
    
    這裡我們的起始點皆為 0, 有一些演算法會用1當起點
    Time Complexity: O(NLogN) (heapify 執行 LogN次 * 總共 N個node) / Space Complexity:O(1) (As in-place method)
    https://www.youtube.com/watch?v=j-DqQcNPGbE
    
"""
