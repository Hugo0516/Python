from typing import List

# class Solution:
#     def largestRectangleArea(self, heights: List[int]) -> int:
#         stack = list()
#         res = 0
#         heights.append(0)
#         N = len(heights)
#         for i in range(N):
#             print(not stack)
#             if not stack or heights[i] > heights[stack[-1]]:
#                 stack.append(i)
#             else:
#                 print(stack, heights[i], stack and heights[i])
#                 while stack and heights[i] <= heights[stack[-1]]:
#                     h = heights[stack[-1]]
#                     stack.pop()
#                     w = i if not stack else i - stack[-1] - 1
#                     res = max(res, h * w)
#                 stack.append(i)
#         return res

"""
下面的比較好理解，速度也比較快
https://blog.csdn.net/fuxuemingzhu/java/article/details/82977472
"""


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        stack.append(-1)
        res = 0
        l = len(heights)
        for i in range(l):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:  # heights[stack[-1]] >= heights[i] 表示bar沒有遞增惹
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))  # i - stack[-1] - 1 很簡單
            stack.append(i)
        while stack[-1] != -1:  # 因為我們要嚴格遞增，所以"剩下"還在stack的數字都是嚴格遞增，
            # 也因為要嚴格遞增所以就算後面一個跟上一個一樣大，我們也要先pop上一個出來且計算面積
            res = max(res, heights[stack.pop()] * (l - stack[-1] - 1))
        return res


"""
    解題思路：
            Save index in the stack as height may have the same value.
            Based on heights, maintain an increasing stack!!!!!!!!!!! 
            (Must be strictly increasing in this case to help us solve the problem)
            
            All the bars between i and j should be greater or equal than heights[j]
            The final increasing stack should contain the last bar.
            heights[stack.pop] * (n - stack.peek() - 1)
            
            Time Complexity = O(n), Space Complexity = O(n)
            
            Input: [2,1,5,6,2,3]
            Output: 10
            https://www.youtube.com/watch?v=GYuBQacXr1A
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 1, 5, 6, 2, 3]

    print(demo.largestRectangleArea(input_1), end='')
