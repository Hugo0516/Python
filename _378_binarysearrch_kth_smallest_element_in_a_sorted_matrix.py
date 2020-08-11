import heapq
from bisect import bisect
from typing import List


class Solution:
    # priority queue 作法
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for line in matrix:
            nums.extend(line)
        heapq.heapify(nums)     # 複習 heapq 用法!!!
        res = 0
        for i in range(k):
            res = heapq.heappop(nums)

        return res

    # binary search 版本
    def kthSmallest2(self, matrix: List[List[int]], k: int) -> int:
        lo, hi = matrix[0][0], matrix[-1][-1]
        while lo <= hi:
            mid = (lo + hi) >> 1
            loc = sum(bisect.bisect_right(m, mid) for m in matrix)
            if loc >= k:
                hi = mid - 1
            else:
                lo = mid + 1
        return lo

    def kthSmallest3(self, matrix: List[List[int]], k: int) -> int:
        nums = []
        for line in matrix:
            nums.extend(line)
        nums.sort()
        res = 0
        for i in range(k):
            res = nums.pop(0)
        return res

"""
    t.ly/Vo3z
"""

if __name__ == "__main__":
    demo = Solution()
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    k = 8

    print(demo.kthSmallest(matrix, k))
    print(demo.kthSmallest3(matrix, k))
