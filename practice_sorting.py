def bubble_sort(data):
    for i in range(0, len(data) - 1):
        for j in range(0, len(data) - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


data_1 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
bubble_sort(data_1)
print(data_1)


def insertion_sort(data):
    for i in range(1, len(data)):
        j = i - 1
        element = data[i]

        while element < data[j] and j >= 0:
            data[j + 1] = data[j]
            j = j - 1
        data[j + 1] = element


data_2 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
insertion_sort(data_2)
print(data_2)


def selection_sort(data):
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[j] < data[i]:
                data[i], data[j] = data[j], data[i]


data_3 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
selection_sort(data_3)
print(data_3)


def merge(data, left, mid, right):
    l_length = mid - left + 1
    r_length = right - mid
    left_list = [0] * l_length
    right_list = [0] * r_length

    for i in range(l_length):
        left_list[i] = data[left + i]
    for i in range(r_length):
        right_list[i] = data[mid + 1 + i]
    i, j, k = 0, 0, left

    while i < l_length and j < r_length:
        if left_list[i] < right_list[j]:
            data[k] = left_list[i]
            i += 1
        else:
            data[k] = right_list[j]
            j += 1
        k += 1

    while i < l_length:
        data[k] = left_list[i]
        k += 1
        i += 1

    while j < r_length:
        data[k] = right_list[j]
        k += 1
        j += 1


def merge_sort(data, left, right):
    if left < right:
        mid = (left + right) // 2
        merge_sort(data, left, mid)
        merge_sort(data, mid + 1, right)
        merge(data, left, mid, right)


data_4 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
merge_sort(data_4, 0, len(data_4) - 1)
print(data_4)


def quick_sort(data, left, right):
    if left < right:
        i = left
        j = right
        key = data[left]

        while i != j:
            while data[j] > key and i < j:
                j -= 1
            while data[i] <= key and i < j:
                i += 1
            if i < j:
                data[i], data[j] = data[j], data[i]
        data[left], data[i] = data[i], data[left]

        quick_sort(data, left, i - 1)
        quick_sort(data, i + 1, right)


data_5 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
quick_sort(data_5, 0, len(data_5) - 1)
print(data_5)


def heapify(data, length, index):
    if index > length:
        return
    c1 = 2 * index + 1
    c2 = 2 * index + 2
    max = index
    if c1 < length and data[c1] > data[max]:
        max = c1
    if c2 < length and data[c2] > data[max]:
        max = c2
    if max != index:
        data[max], data[index] = data[index], data[max]
        heapify(data, length, max)


def build_heap(data):
    last_node = len(data) - 1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify(data, len(data), i)


def heap_sort(data):
    build_heap(data)

    for i in range(len(data) - 1, -1, -1):
        data[i], data[0] = data[0], data[i]
        heapify(data, i, 0)


data_6 = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
heap_sort(data_6)
print(data_6)
