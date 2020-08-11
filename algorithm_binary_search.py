# binary search implementation is a divide and conquer method
def bsearch(list, val):
    list_size = len(list) - 1

    idx0 = 0
    idxn = list_size
    # Find the middle most value

    while idx0 <= idxn:
        midval = (idx0 + idxn) // 2

        if list[midval] == val:
            return midval
        # Compare the value the middle most value
        if val > list[midval]:
            idx0 = midval + 1
        else:
            idxn = midval - 1

    # if idx0 > idxn:
    #     return None


# Initialize the sorted list
list = [2, 7, 19, 34, 53, 72]

# Print the search result
print(bsearch(list, 72))
print(bsearch(list, 11), '\n')


# binary search recursion edition:
def bsearch2(list, idx0, idxn, val):
    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
        # Compare the search item with middle most value

        if list[midval] > val:
            return bsearch2(list, idx0, midval - 1, val)
        elif list[midval] < val:
            return bsearch2(list, midval + 1, idxn, val)
        else:
            return midval


list = [8, 11, 24, 56, 88, 131]
print(bsearch2(list, 0, 5, 56))
print(bsearch2(list, 0, 5, 51))

"""
    Divide and Conquer:
    In divide and conquer approach, the problem in hand, is divided into smaller sub-problems and then each problem is solved independently.
    When we keep on dividing the subproblems into even smaller sub-problems,
    we may eventually reach a stage where no more division is possible.
    Those "atomic" smallest possible sub-problem (fractions) are solved.
    The solution of all sub-problems is finally merged in order to obtain the solution of an original problem.
    
    Time Complexity: O(logN)
    
    Binary search 使用前提： 那個東西要先排序過！！！！！！！！！
    
    Broadly, we can understand divide-and-conquer approach in a three-step process.:
    1. Divide/Break
    2. Conquer/Solve
    3. Merge/Combine
"""
