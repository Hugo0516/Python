from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = []
        nums.sort()  # sort 為了讓 nums 有規律 更有循環
        # 1 2 3 4 5 6
        for i in range(n - 2):
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:  # 最小的三個都相加惹還 >0 那就一定找不到
                break
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:  # 最大的兩個都相加惹還 <0
                continue
            if 0 < i and nums[i] == nums[i - 1]:  # [-100, 0, 0, 20, 20, 80]
                continue  # 可能全部是0 , 或是找不到任何解法

            left, right = i + 1, n - 1  # 這裡是用左右兩邊往中間靠攏的方式，為什麼呢？
            # 聽影片是說如果我們按造以前固定左邊然後持續便利到最右邊的話時間複雜度是n^2
            # 兩頭往中間找的話，可以減少我們的時間複雜度(或是說intuition time)

            while left < right:
                tmp = nums[i] + nums[left] + nums[right]
                if tmp == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left + 1 < right and nums[left] == nums[left + 1]:  # 左邊的推到更右邊
                        left += 1
                    left += 1  # 更新數字，這樣下次跑while loop 就會是全新的數字惹
                    while left < right - 1 and nums[right] == nums[right - 1]:  # 右邊的推到更左邊
                        right -= 1
                    right -= 1
                elif tmp < 0:  # 左邊數字佔的比重太高 or 太小了
                    left += 1
                else:  # 右邊數字佔的比重太高 or 太小了 (because tmp > 0)
                    right -= 1
        return res


"""
    解題思路：
            Fang 重要題
            Given array nums = [-1, 0, 1, 2, -1, -4],   [-4, -1, -1, 0, 1, 2]
            A solution set is: [[-1, 0, 1], [-1, -1, 2]]
            
            1. [0, 1, 2, 3, 4, ...] => 0+1+2+2 = 3 > 0
            2. [-100, 0, 1, 2, 3, ..., 8, 9] => -100+8+9 = -83 < 0
            continue ... get rid of -100, start from 0, then we will jump back 1.
            
            Time Complexity: O(n) / Space Complexity: O(1)
            
            https://www.youtube.com/watch?v=CW6G30xQCbw
    
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [-1, 0, 1, 2, -1, -4]
    print(demo.threeSum(input_1))
