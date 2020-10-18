from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        res = nums[0] + nums[1] + nums[len(nums) - 1]

        for i in range(len(nums) - 2):  # 因為: 可以往左邊縮進的最高位置就是 len(nums) - 2 ( for 循環的目的是為了逼近 target 值)
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if abs(val - target) < abs(res - target):
                    res = val  # 更新
                if val == target:
                    return target
                elif val < target:
                    left += 1
                else:
                    right -= 1
        return res

    # 我自己寫的, 記住這個方法
    # Time Complexity: O(n^2) / Space Complexity: O(n^2 / 2) (S.C我自己算的, 可知這複雜度不是很好= =)
    def threeSumClosest2(self, nums: List[int], target: int) -> int:
        # [-1, 2, 1, -4] => [-4, -1, 1, 2]
        nums.sort()
        ans = 999999
        dict_1 = {}

        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                temp = nums[i] + nums[left] + nums[right]
                if temp == target:
                    return temp
                elif temp < target:
                    res_1 = target - temp
                    if res_1 < ans:
                        ans = res_1
                        dict_1[ans] = [nums[i], nums[left], nums[right]]
                    left += 1
                elif temp > target:
                    res_1 = temp - target
                    if res_1 < ans:
                        ans = res_1
                        dict_1[ans] = [nums[i], nums[left], nums[right]]
                    right -= 1
        return sum(dict_1[ans])


"""
    解題思路：
            sorted nums: [-4, -1, 1, 2]
            result = (-4) + (-1) + 2 (為了要跟target 做比較，然後慢慢向中間縮進，接著找到最接近target的值)
            result > target :(表最右邊的值(2)可能選大惹) -4 -1 1(所以右邊的值，往左邊移一位，所以2變1)
            result < target : 把左邊的值，向右移一位 -4 -1 1(左邊的直往右移)
            
            Time Complexity: O(n^2) / Space Complexity: O(1) (待確認！)
            
            https://www.youtube.com/watch?v=F4UKF07-tvo
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [-1, 2, 1, -4]
    target = 1
    print(demo.threeSumClosest(input_1, target))

    print(demo.threeSumClosest2([1, 1, 1, 0], -100))
