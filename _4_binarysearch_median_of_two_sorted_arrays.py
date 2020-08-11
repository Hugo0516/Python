from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        if n1 > n2:
            return self.findMedianSortedArrays(nums2, nums1)

        k = (n1 + n2 + 1) // 2
        l = 0
        r = n1

        while l < r:
            m1 = l + (r - l) // 2
            m2 = k - m1
            # print(m1, m2)
            # print(nums1[int(m1)], nums2[int(m2-1)])
            if nums1[int(m1)] < nums2[int(m2 - 1)]:
                l = m1 + 1
            else:
                r = m1
            # print(l, r)

        m1 = l
        m2 = k - l

        # print(m1, m2)
        # print('c1這邊ㄉ',nums1[int(m1-1)], nums2[int(m2-1)])
        c1 = max(float('-inf') if m1 <= 0 else nums1[int(m1 - 1)],
                 float('-inf') if m2 <= 0 else nums2[int(m2 - 1)])  # m1 <= 0 表沒有這個索引
        if (n1 + n2) % 2 == 1:
            return c1

        # print('c2這邊ㄉ',nums1[int(m1-1)], nums2[int(m2-1)], m1, m2)
        c2 = min(float('inf') if m1 >= n1 else nums1[int(m1)],
                 float('inf') if m2 >= n2 else nums2[int(m2)])      # m1 >= n1 表超出input_1總大小
        # print(c1, c2)

        return (c1 + c2) * 0.5

"""
    解題思路：
            求出中位數的整數k, 為啥是整數呢？反正之後還會判斷k是否為整數(line 32)，只是先用k為整數下去算
            l 當作 n1左邊界，r 當作 n1最右邊；藉此慢慢往中間靠攏找出m1
            m1 + m2 = k, num[m1] > num[m2-1]代表 才可以確保：C(k-1) = max(A(m1-1), B(m2-1)), C(k) = min(A(m1), B(m2))
            m1, m2 是代表m1, m2個，並不是指索引m1, m2
            Binary search m1, based on a[m1] <? b[m2-1]
            
            Time complexity: O(log(min(n1,n2)))/ Space complexity: O(1)
            
            https://www.youtube.com/watch?v=KB9IcSCDQ9k
            
"""

if __name__ == '__main__':
    demo = Solution()
    input1 = [1, 2]
    input2 = [3, 4]
    print(demo.findMedianSortedArrays(input1, input2))