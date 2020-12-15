from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result


"""
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

和 53 很像, 但是有許多額外的點要注意！！！！ (Zero & Negative Numbers)
Zero, 會毀了過去所有解果
Negative, 會讓以前最大的變最小, 但我們可以在後面期待另一個 Negative, 將它變會來

Time Complexity: O(N), where N is the size of nums. The algorithm achieves linear runtime since we are going through nums only once.

Space Complexity: O(1), since no additional space is consumed rather than variables which keep track of the maximum product so far, 
the minimum product so far, current variable, temp variable, and placeholder variable for the result.

*** 這題還是採用 in-place 的高級算法  ***
"""
if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 3, -2, 4]
    input_2 = [-2, 0, -1]
    input_3 = [2]
    input_4 = [-3, -1, -1]

    print(demo.maxProduct(input_1))
    print(demo.maxProduct(input_2))
    print(demo.maxProduct(input_3))
    print(demo.maxProduct(input_4))
