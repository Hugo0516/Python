def p(nums, d, n, used, curr, ans):
    if d == n:
        ans.append(curr)
        return

    for i in range(len(nums)):
        if used[i]:
            continue
        used[i] = True
        curr.append(nums[i])
        p(nums, d + 1, n, used, curr[:], ans)
        curr.pop()
        used[i] = False

"""
    #11 一定要用curr[:], 不然的話之後的curr.pop(), 會影響原本已經在ans的答案
    EX:
    cur[:] 版本: ans = [1, 2, 3]
                curr.pop => ans = [1 ,2, 3]
    cur 版本: ans = [1, 2, 3]
            curr.pop() => ans = [1, 2]
    
    可以和 113 題對照!!!!    
"""

ans_1 = []
p([1, 2, 3], 0, 3, [False] * 3, [], ans_1)
print(ans_1)
