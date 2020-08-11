def quick_sort(A):
    quick_sort2(A, 0, len(A) - 1)


def quick_sort2(A, low, hi):  # 如果每次都剛好1/2 那Time Complexity = O(LogN), 如果是很極端就O(N)
    if low < hi:
        p = partition(A, low, hi)  # 假如每一次很極端選到 p=len(A) - 2
        quick_sort2(A, low, p - 1)  # 那這一行就要跑 n 次 所以0+...+n = n^2
        quick_sort2(A, p + 1, hi)  # 那這行每次都只剩下一個 所以 O(1)


def get_pivot(A, low, hi):
    mid = (hi + low) // 2
    pivot = hi
    if A[low] < A[mid]:
        if A[mid] < A[hi]:
            pivot = mid
    elif A[low] < A[hi]:
        pivot = low
    return pivot


def partition(A, low, hi):  # 因為29, Time Complexity = O(N)
    pivotIndex = get_pivot(A, low, hi)
    pivotValue = A[pivotIndex]
    A[pivotIndex], A[low] = A[low], A[pivotIndex]
    border = low

    for i in range(low, hi + 1):
        if A[i] < pivotValue:
            border += 1
            A[i], A[border] = A[border], A[i]
    A[low], A[border] = A[border], A[low]

    return border


def quicksort(data, left, right):  # 輸入資料，和從兩邊開始的位置
    if left >= right:  # 如果左邊大於右邊，就跳出function
        return

    i = left  # 左邊的代理人
    j = right  # 右邊的代理人
    key = data[left]  # 基準點

    while i != j:
        while data[j] > key and i < j:  # 從右邊開始找，找比基準點小的值!!!!
            j -= 1
        while data[i] <= key and i < j:  # 從左邊開始找，找比基準點大的值!!!!
            i += 1
        if i < j:  # 當左右代理人沒有相遇時，互換值
            data[i], data[j] = data[j], data[i]

            # 將基準點歸換至代理人相遇點
    data[left] = data[i]
    data[i] = key
    # 這時候 i == j
    quicksort(data, left, i - 1)  # 繼續處理較小部分的子循環
    quicksort(data, i + 1, right)  # 繼續處理較大部分的子循環


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    quick_sort(arr)
    print(arr, '\n')

    data = [89, 34, 23, 78, 67, 100, 66, 29, 79, 55, 78, 88, 92, 96, 96, 23]
    data_2 = [55, 95, 91, 66, 11, 96, 14, 62, 44, 75]
    quicksort(data_2, 0, len(data_2) - 1)
    print(data_2)

"""
    Time Complexity: O(N * logN)第一個基準值的位置剛好是中位數，將資料均分成二等份(左邊字串列大小=右邊字串列大小) or 
    O(N^2)當資料的順序恰好為由大到小或由小到大時有分割跟沒分割一樣
    Space Complexity: O(Log N) 所以比 merge sort(Space Complexity: O(N)) 好
    因為要 call stack frame, 所以最差的SC: 為O(N), 但只要compiler有支援尾端呼叫最佳化(tail-call optimization)
    那就只要O(LogN)
    
    https://rust-algo.club/sorting/quicksort/
    
    I use the median of the three to optimize the Time Complexity
    https://www.youtube.com/watch?v=CB_NCoxzQnk
    
    --------------------------------------------------------------------
    記住 quicksort() !!!!
    快速排序 (Quick Sort) 的想法是說，先找一個基準點，然後派兩個代理人分別從資料的兩邊開始往中間找，
    如果右邊找到一個值比基準點小，左邊找到一個值比基準點大，就讓他們互換。反覆找並互換，直到兩個人相遇。
    然後再將相遇的點跟基準點互換。第一輪結束。
    https://ithelp.ithome.com.tw/articles/10202330?sc=iThelpR
"""
