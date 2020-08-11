from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        nums1[:n] = nums2[:n]   # 這裡和 第10行呼應


"""
    這個題的核心是注意到兩個數組是已經有序的！這樣就可以很簡單的解決。

    方法是在每個數組的最後一個指定位置判斷大小，根據判定的大小放到nums1的最後位置裡，然後移動指針，繼續判斷，直到一個數組先遍歷結束。
    
    注意，如果nums1已經遍歷結束了，就要把nums2剩下的元素放到nums1的前面。最後可以確保有序。

    https://blog.csdn.net/fuxuemingzhu/java/article/details/77444695
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3, 0, 0, 0]
    input_2 = [2, 5, 6]

    num_1 = 3
    num_2 = 3

    demo.merge(input_1, num_1, input_2, num_2)
    print(input_1)