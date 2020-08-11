def combination(nums, degree, n, start, curr, ans):
    if degree == n:
        ans.append(curr)
        return

    for i in range(start, len(nums)):
        curr.append(nums[i])
        combination(nums, degree + 1, n, i + 1, curr[:], ans)
        curr.pop()

"""
    degree = 遞迴深度, n = 答案允許長度, i+1 = 因為之前取過的不能再取
    https://www.youtube.com/watch?v=zIY2BWdsbFs
"""

ans_1 = []
combination([1, 2, 3], 0, 3, 0, [], ans_1)
print(ans_1)

ans_2 = []
combination([1, 2, 3], 0, 2, 0, [], ans_2)
print(ans_2)