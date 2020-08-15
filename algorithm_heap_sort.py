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


def build_heap(array):  # build_heap 的 time complexity = O(LogN)
    last_node = len(array) - 1
    parent = (last_node - 1) // 2
    for i in range(parent, -1, -1):
        heapify2(array, len(array)-1, i)    # 不確定這裡是 len(array) or len(array)-1


def heap_sort2(array):
    length = len(array)
    build_heap(array)   # O(LogN)

    for i in range(length - 1, -1, -1):     # O(NLogN)
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
    
    Heap Sort 好處：相較 merge sort, heap sort 是用in-place 的方法，不用浪費額外空間!!!
    
    給一個 array 做 heap sort 一定得從 0 開始， 不是 datastructure_max_heap 可以自己設從 1 開始 
    (因為 datastructure_max_heap 是自己寫insert函數，所以可以自己亂搞)
    
    小問題：
        heap_sort 一樣是希望輸出 可以由小到大，但是教科書的作法都是先將array 變成 max_heap，
        然後藉由root 和 最後一個對調，對調後將總長-1(排除最大)，然後做heapify 
        可是為什麼不直接將heapify 寫成 min 版本的heapify 呢？
        
    Heapsort 的特性如下：

    使用 heap 資料結構輔助，通常使用 binary heap。
    不穩定排序：排序後，相同鍵值的元素相對位置可能改變。
    原地排序：不需額外花費儲存空間來排序。
    較差的 CPU 快取：heap 不連續存取位址的特性，不利於 CPU 快取。
    
    
        
    
"""
