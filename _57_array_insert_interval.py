from typing import List

import interval as Interval


class Solution:
    def insert(self, intervals: List[List[int]],
               newInterval: List[int]) -> List[List[int]]:
        index = len(intervals)
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                index = i
                break

        intervals.insert(index, newInterval)

        ans = []
        for interval in sorted(intervals, key=lambda x: x[0]):  # sorted()會保留原List, 而是copy一個之後再list出來
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
                print(ans[-1][1])
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans

    # def insert2(self, intervals, newInterval):
    #     start, end = newInterval.start, newInterval.end
    #     l, r = [], []
    #     for interval in intervals:
    #         if interval.end < start: l += interval,
    #         elif interval.start > end: r += interval,
    #         else:
    #             start = min(start, interval.start)
    #             end = max(end, interval.end)
    #     return l + [Interval(start, end)] + r


"""
    http://zxi.mytechroad.com/blog/geometry/leetcode-57-insert-interval/
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[1, 3], [6, 9]]
    ninput_1 = [2, 5]

    input_2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
    ninput_2 = [4, 8]

    print(demo.insert(input_1, ninput_1))
    print(demo.insert(input_2, ninput_2))

    # print(demo.insert2(input_1, ninput_1))
