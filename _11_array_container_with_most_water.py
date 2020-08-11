from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans, l, r = 0, 0, len(height) - 1   # l = left, r = right

        while l < r:
            h = min(height[l], height[r])
            ans = max(ans, h * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans


"""
    解題思路：
            Solution 1.: Brute force (Time Complexity: O(n^2))
            Solution 2.: Two pointers
            Start with l=0, r=n-1, the widest container
            Input: [1,8,6,2,5,4,8,3,7] / Output: 49
            Time Complexity: O(n) / Space Complexity: O(1)
            
            https://www.youtube.com/watch?v=IONgE6QZgGI
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(demo.maxArea(input_1))
