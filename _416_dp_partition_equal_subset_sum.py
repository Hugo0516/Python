from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        tmp = sum(nums)

        if tmp % 2 != 0:
            return False
        else:
            subSetSum = tmp // 2
            n = len(nums)
            dp = [[False for i in range(subSetSum + 1)] for j in range(n + 1)]
            dp[0][0] = True

            for i in range(1, n + 1):  # 1~4
                curr = nums[i - 1]
                for j in range(subSetSum + 1):  # 0~11
                    if j < curr:  # j < curr, 表示新加入的 subset 沒辦法滿足和=j, 因為自己一個就超過 j 了
                        dp[i][j] = dp[i - 1][j]
                    else:  # if j > curr, 表示有機會滿足 subset 和為j
                        dp[i][j] = dp[i - 1][j] | dp[i - 1][j - curr]   # 即為轉移方程式
            return dp[n][subSetSum]

    # We could further optimize Approach 3. We must understand that for any array element i,
    # we need results of the previous iteration (i-1) only.
    # Hence, we could achieve the same using a one-dimensional array as well.
    def canPartition2(self, nums: List[int]) -> bool:
        if len(nums) == 0:
            return False
        tmp = sum(nums)

        if tmp % 2 != 0:
            return False

        subSetSum = tmp // 2
        dp = [False for i in range(subSetSum + 1)]
        dp[0] = True

        for curr in nums:
            for j in range(subSetSum, curr - 1, -1):
                dp[j] |= dp[j - curr]   # 轉移方程式

        return dp[subSetSum]


"""
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

DP 的定義非常重要！！！
x = 子集, EX: {3} 的子集為 {}{3}
y = sum, 看 x 所代表的子集合是否加起來能等於 y
EX: dp[2][3] = True , 因為 {3, 4} 的子集可以達到 3

tmp+1              0 1 2 3 4 5
                ------------------
n       {}     |
+      {3}     |
1     {3,4}    |
     {3,4,2}   |
    {3,4,2,1}  |

We maintain a 2D array , dp[n][subSetSum] For an array element i and sum j in array nums,
dp[i][j]=true if the sum j can be formed by array elements in subset nums[0]..nums[i],
otherwise dp[i][j]=false

dp[i][j] is true it satisfies one of the following conditions :

Case 1) sum j can be formed without including ith element, if dp[i−1][j]==true

Case 2) sum j can be formed including ith  element, if dp[i−1][j−nums[i]]==true

Time Complexity: O(m*n), m = tmp, n is the number of array
Space Complexity: O(m*n)
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 5, 11, 5]  # [1, 5, 5] / [11]
    print(demo.canPartition(input_1))
    input_2 = [1, 2, 3, 4]
    input_3 = [1, 1, 3, 4, 7]
    input_4 = [2, 3, 4, 6]
    print(demo.canPartition(input_2))
    print(demo.canPartition(input_3))
    print(demo.canPartition(input_4))
    input_5 = [3, 3, 3, 4, 5]
    print(demo.canPartition(input_5))

    print()
    print(demo.canPartition2(input_1))
    print(demo.canPartition2(input_2))
    print(demo.canPartition2(input_3))
    print(demo.canPartition2(input_4))
