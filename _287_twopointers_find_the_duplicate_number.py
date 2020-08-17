from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[nums[0]]
        while slow != fast:
            fast = nums[nums[fast]]
            slow = nums[slow]
        fast = 0
        while slow != fast:
            fast = nums[fast]
            slow = nums[slow]
        return fast

    def findDuplicate2(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = (l + r) // 2
            count = 0
            for i in nums:
                if i <= mid:
                    count += 1
            if count <= mid:
                l = mid + 1
            else:
                r = mid
        return r


"""
    第二個方法比較好
    幹你老師 都好難想＝＝ 雞掰
    
    思路是我們在[1,N]範圍內先求出mid，再統計小於等於mid的數字個數count，如果count<=mid，說明重複數字在[mid+1,N]中，否則在[1 ,mid)中。
    可能不明白為什麼這麼移動左右指針，所以，我做一下說明：

    我們統計小於等於mid的數字個數count，當nums在[1,mid]雙閉區間中的數字不存在重複時，count應該恰好等於mid；
    當nums在[1,mid]雙閉區間中的數字存在重複時，count應該>mid；
    當nums在[1,mid]雙閉區間中的數字存在遺漏時，count應該<mid。
    所以，當我們發現count <= mid時，說明重複數字在[mid + 1, N]中，否則在[1,mid)中。
    
    t.ly/FRPn
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 3, 4, 2, 2]
    print(demo.findDuplicate2(input_1))
