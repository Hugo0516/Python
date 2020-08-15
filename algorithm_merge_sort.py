# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    # create temp arrays
    L = [0] * n1
    R = [0] * n2

    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    # Merge the temp arrays back into arr[l..r]
    i = 0  # Initial index of first subarray
    j = 0  # Initial index of second subarray
    k = l  # Initial index of merged subarray

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


# l is for left index and r is right index of the
# sub-array of arr to be sorted
def mergeSort(arr, l, r):
    if l < r:
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = (l + (r - 1)) // 2

        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m + 1, r)
        merge(arr, l, m, r)

    # Driver code to test above


arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
print("Given array is")
print(arr, '\n')

mergeSort(arr, 0, n - 1)
print("\n\nSorted array is")
print(arr)

"""
    Time Complexity, Space Complexity 分析:
    透過遞迴關係式，很容易計算 Mergesort 的時間複雜度。假設排序長度為 n 的序列最多需要 T(n) 時間。可以觀察到，如果序列只有一個元素，
    Mergesort 僅需要常數時間就可以完成排序，寫成 T(n)=1。
    如果 n>2，Mergesort 會將序列分為 ⌈n2⌉ 部分，以及 ⌊n2⌋ 部分。我們可以將排序前者寫成 T(⌈n2⌉)，而後者花費時間為 T(⌊n2⌋)。

    最後，合併兩個子序列僅需 n 個操作。可得下列遞迴關係式。
    (為了方便計算，把 floor 和 ceil 捨去）

    T(n)={1 if n=1, 2T(n2)+notherwise.
    根據 Master Theorem，可得複雜度為 O(nlogn)。
    
    Space Complexity    
    Mergesort 的缺點之一就是在合併子序列時，需要額外的空間依序插入排序資料 !!!!!!!!!!!!!!
    若是遞迴版本的 Mergesort 還需額外加上遞迴花費的 call stack 空間，因此額外空間複雜度為 O(n)+O(logn)=O(n)（以陣列實作）。
    
    高效穩定：最佳、平均，與最差時間複雜度皆為 $O(n \log n) $。
    穩定排序：相同鍵值的元素，排序後相對位置不改變。
    非原地排序：除了資料本身，仍需額外花費儲存空間來排序。
    分治演算法：將主問題化作數個子問題，各個擊破。
    
    https://rust-algo.club/sorting/mergesort/index.html
    https://www.geeksforgeeks.org/python-program-for-merge-sort/
"""