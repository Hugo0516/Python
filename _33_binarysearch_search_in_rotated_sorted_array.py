from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2    # 這頁可以改成(right+left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid] > target >= nums[left]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1


""" 
    明顯也是二分查找!!!!!!!!!!!
    這一題細節比較不好想= =
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79534213
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [4, 5, 6, 7, 0, 1, 2]
    print(demo.search(input_1, 0))