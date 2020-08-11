def p(nums, degree, n, used, curr, ans):
    if degree == n:
        ans.append(curr)
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        curr.append(nums[i])
        p(nums, degree + 1, n, used, curr[:], ans)
        curr.pop()
        used[i] = False


"""
    #11 一定要用curr[:], 不然的話之後的curr.pop(), 會影響原本已經在ans的答案
    
    d 表示 遞迴深度, n 表示我要娶幾個數字出來排列 !!
    
    EX:
    cur[:] 版本: ans = [1, 2, 3]
                curr.pop => ans = [1 ,2, 3]
    cur 版本: ans = [1, 2, 3]
            curr.pop() => ans = [1, 2]
    
    https://www.youtube.com/watch?v=zIY2BWdsbFs
    
    可以和 113 題對照!!!!    
    
    
    0-1-2    1-0-2    2-0-1
     \        \        \
      2-1      2-0      1-0 
"""

ans_1 = []
p([1, 2, 3], 0, 3, [False] * 3, [], ans_1)
print(ans_1)

ans_2 = []
p([1, 2, 3], 0, 2, [False] * 3, [], ans_2)
print(ans_2)
