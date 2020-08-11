from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for interval in sorted(intervals, key=lambda x: x[0]):  # sorted()會保留原List, 而是copy一個之後再list出來
            if not ans or interval[0] > ans[-1][1]:
                ans.append(interval)
                print(ans[-1][1])
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])
        return ans


"""
    list 的sort 方法返回的是對已經存在的列表進行操作，無返回值，
    而內建函數sorted 方法返回的是一個新的list，而不是在原來的基礎上進行的操作。
    Time Complexity: O(N*logN) / Space Complexity: O(N)
    
    http://zxi.mytechroad.com/blog/geometry/leetcode-56-merge-intervals/
    https://www.youtube.com/watch?v=6tLHjei-f0I    
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(demo.merge(input_1))
