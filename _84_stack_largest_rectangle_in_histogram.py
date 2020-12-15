from typing import List


class Solution:
    # stack solution
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = list()
        stack.append(-1)
        res = 0
        l = len(heights)
        for i in range(l):
            while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:  # heights[stack[-1]] >= heights[i] 表示bar沒有遞增惹
                res = max(res, heights[stack.pop()] * (i - stack[-1] - 1))
                # i - stack[-1] - 1 很簡單
                # 要注意, 會先 pop 出來!!!!
            stack.append(i)
        while stack[-1] != -1:  # 因為我們要嚴格遞增，所以"剩下"還在stack的數字都是嚴格遞增，
            # 也因為要嚴格遞增所以就算後面一個跟上一個一樣大，我們也要先pop上一個出來且計算面積
            res = max(res, heights[stack.pop()] * (l - stack[-1] - 1))
        return res


# Brute Force
class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i, len(heights)):
                min_height = float('inf')
                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])
                max_area = max(max_area, min_height * (j - i + 1))

        return max_area


# better Brute Force
class Solution3:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        for i in range(len(heights)):
            min_height = float('inf')
            for j in range(i, len(heights)):
                for k in range(i, j + 1):
                    min_height = min(min_height, heights[k])
                maxarea = max(maxarea, min_height * (j - i + 1))

        return maxarea


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
    
    這一題解法要特別記下來!!!!!!!, 看籃子王
    Approach 1:
    Time Complexity: O(n), n numbers are pushed and popped
    Space Complexity:O(n), stack is used.
    
    Approach 2:
    Time Complexity: O(n^3), We have to find the minimum height bar O(n) lying between every pair O(n^2 ).
    Space Complexity: O(1), constant space is used.
    
    Approach 3:
    Time Complexity: O(n^2), Every possible pair is considered
    Space Complexity: O(1), No extra space is used. 
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 1, 5, 6, 2, 3]

    print(demo.largestRectangleArea(input_1))

    demo2 = Solution2()
    print(demo2.largestRectangleArea(input_1))

    demo3 = Solution3()
    print(demo3.largestRectangleArea(input_1))
