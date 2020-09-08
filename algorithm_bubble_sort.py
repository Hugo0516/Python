def bubble_sort(data):
    # Swap the elements to arrange in order
    data = [99, 39, 100, 22, 41, 63]
    for iter_num in range(0, len(data) - 1):  # # 有 n 個資料長度，但只要執行 n-1 次
        for idx in range(0, len(data) - 1 - iter_num):
            if data[idx] > data[idx + 1]:
                data[idx], data[idx + 1] = data[idx + 1], data[idx]


list = [19, 2, 31, 45, 6, 11, 121, 27]
bubble_sort(list)
print(list)

"""
    Time Complexity: O(N)當資料的順序恰好為由小到大時 or O(N^2)當資料的順序恰好為由大到小時
    注意是到：倒數第二個！！
    
    in-place 作法~ 
    
    https://rust-algo.club/sorting/bubble_sort/index.html
    https://www.youtube.com/watch?v=YHm_4bVOe1s
"""