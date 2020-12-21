from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        nums.sort()
        target, rem = divmod(sum(nums), k)
        if rem or nums[-1] > target: return False

        dp = [False] * (1 << len(nums))
        dp[0] = True
        total = [0] * (1 << len(nums))

        for state in range(1 << len(nums)):
            if not dp[state]: continue
            for i, num in enumerate(nums):
                future = state | (1 << i)
                if state != future and not dp[future]:
                    if (num <= target - (total[state] % target)):
                        dp[future] = True
                        total[future] = total[state] + num
                    else:
                        break
        return dp[-1]


class Solution2:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        visited = [False] * len(nums)

        def backtrack(nums, k, target, sum, index, visited):
            if k == 0:
                return True
            if sum > target:
                return False
            if sum == target:
                return backtrack(nums, k - 1, target, 0, 0, visited)

            for i in range(index, len(nums)):
                if not visited[i]:
                    sum += nums[i]
                    visited[i] = True
                    if backtrack(nums, k, target, sum, i + 1, visited):
                        return True

                    sum -= nums[i]
                    visited[i] = False
            return False

        return backtrack(nums, k, total / k, 0, 0, visited)



"""
Sol 1: DP <Leetcode>
我沒看, 因為我覺得用 backtrack 比較好

Sol 2: Backtrack
Time Complexity: O( k * 2^n )
Space Complexity: O(n)

Reference: https://www.youtube.com/watch?v=JyYZ1j3Uv0E
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/discuss/180014/Backtracking-Thinking-Process

"""

if __name__ == '__main__':
    demo = Solution()
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print(demo.canPartitionKSubsets(nums, k))

    nums = [4, 3, 2, 3, 5, 2, 1]
    demo2 = Solution2()
    print(demo2.canPartitionKSubsets(nums, k))
