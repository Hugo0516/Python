from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        left, right = 0, N - 1

        while left <= right:
            while left < right and nums[left] == nums[right]:
                # left +1 的用意就是, 因為裡面有相同的, 所以+1 可以把搜索長度變小(我自己這樣認為啦)
                left += 1

            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True

            if nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return False


"""
    https://blog.csdn.net/fuxuemingzhu/java/article/details/83214278
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 5, 6, 0, 0, 1, 2]
    target_1 = 0
    target_2 = 3

    print(demo.search(input_1, target_1))
    print(demo.search(input_1, target_2))
