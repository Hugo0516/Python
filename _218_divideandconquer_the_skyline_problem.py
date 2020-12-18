import heapq
import bisect
from typing import List


class Solution:
    def getSkyline(self, buildings: 'List[List[int]]') -> 'List[List[int]]':
        """
        Divide-and-conquer algorithm to solve skyline problem,
        which is similar with the merge sort algorithm.
        """
        n = len(buildings)
        # The base cases
        if n == 0:
            return []
        if n == 1:
            x_start, x_end, y = buildings[0]
            return [[x_start, y], [x_end, 0]]

        # If there is more than one building,
        # recursively divide the input into two subproblems.
        left_skyline = self.getSkyline(buildings[: n // 2])
        right_skyline = self.getSkyline(buildings[n // 2:])

        # Merge the results of subproblem together.
        return self.merge_skylines(left_skyline, right_skyline)

    def merge_skylines(self, left, right):
        """
        Merge two skylines together.
        """

        def update_output(x, y):
            """
            Update the final output with the new element.
            """
            # if skyline change is not vertical -
            # add the new point
            if not output or output[-1][0] != x:
                output.append([x, y])
            # if skyline change is vertical -
            # update the last point
            else:
                output[-1][1] = y

        def append_skyline(p, lst, n, y, curr_y):
            """
            Append the rest of the skyline elements with indice (p, n)
            to the final output.
            """
            while p < n:
                x, y = lst[p]
                p += 1
                if curr_y != y:
                    update_output(x, y)
                    curr_y = y

        n_l, n_r = len(left), len(right)
        # nL = number of points (or coordinates) in the left skyline;
        # nR = number of points (or coordinates) in the right skyline.
        # they are used to ensure the pL and pR skyline element indices do not go out of bounds.
        p_l = p_r = 0
        curr_y = left_y = right_y = 0
        output = []

        # while we're in the region where both skylines are present
        while p_l < n_l and p_r < n_r:
            point_l, point_r = left[p_l], right[p_r]
            # pick up the smallest x
            if point_l[0] < point_r[0]:
                x, left_y = point_l
                p_l += 1
            else:
                x, right_y = point_r
                p_r += 1
            # max height (i.e. y) between both skylines
            max_y = max(left_y, right_y)
            # if there is a skyline change
            if curr_y != max_y:
                update_output(x, max_y)
                curr_y = max_y

        # there is only left skyline
        append_skyline(p_l, left, n_l, left_y, curr_y)

        # there is only right skyline
        append_skyline(p_r, right, n_r, right_y, curr_y)

        return output


# 這方法太慢, 因為 remove function time complexity 太高
class Solution2:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        points = []

        for l, r, h in buildings:
            points.append([l, -h, 'start'])
            points.append([r, h, 'end'])
        points.sort(key=lambda x: (x[0], x[1]))
        # start before end; start: highest first, end: lowest first
        res, min_heap, pre_height = [], [0], 0

        for point in points:
            if point[2] == 'start':
                heapq.heappush(min_heap, point[1])
            elif point[2] == 'end':
                min_heap.remove(-point[1])  # this operation is too slow
                heapq.heapify(min_heap)
            if pre_height != -min_heap[0]:
                res.append([point[0], -min_heap[0]])
                pre_height = -min_heap[0]
        return res


class Solution3:
    def getSkyline(self, buildings):
        points = []
        for Li, Ri, Hi in buildings:
            points.append((Li, -Hi, 1))
            points.append((Ri, Hi, -1))

        points.sort()
        pq, max_height = [0], 0
        key_points = []
        for x, h, s in points:
            if s == 1:  # start point
                if -h > max_height:
                    max_height = -h
                    key_points.append([x, -h])
                bisect.insort_right(pq, -h)
            else:  # end point
                pq.pop(bisect.bisect_left(pq, h))
                pq_max = pq[-1]
                if pq_max < max_height:
                    max_height = pq_max
                    key_points.append([x, max_height])
        return key_points


"""
Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explanation:
Figure A shows the buildings of the input.
Figure B shows the skyline formed by those buildings. 

The red points in figure B represent the key points in the output list.

solution 1, 為 Leetcode 的官方解答, 但是太複雜了, 寫完一定會有不小心出錯, 所以大家都推第二種寫法
Time Complexity: O(NlogN)
Space Complexity: O(N)

solution 2, 用"掃描線"法, 想法我們因為要一直做高度的比對,所以在做題目的時候, 也要想到一個數據結構, Priority queue(heap),
才可以達到優化我們 插入, 刪除, 查找, 的時間複雜度

solution 3, 與 sol 2 一樣都採用 sweep line, 但是 sol 3的 速度比較快, 因為 sol2 用 remove 拖累時間

Reference:
https://www.youtube.com/watch?v=v5CMa5MUGCo
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
    output_1 = demo.getSkyline(input_1)
    print(output_1)

    demo2 = Solution2()
    output_2 = demo2.getSkyline(input_1)
    print(output_2)

    demo3 = Solution3()
    output_3 = demo3.getSkyline(input_1)
    print(output_3)
