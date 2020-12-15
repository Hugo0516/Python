import math


class Solution:
    # 這是錯的
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        dp = [1] * (n + 1)
        index_a, index_b, index_c = 0, 0, 0
        # [1, 1, 1, 1, 1]
        # [0, 1, 2, 3, 4]
        # [1, 2, 3, 4, 5]
        for i in range(1, n + 1):
            tmp1, tmp2, tmp3 = float('inf'), float('inf'), float('inf')

            if dp[index_a] * a != dp[i - 1]:
                tmp1 = dp[index_a] * a
            if dp[index_b] * b != dp[i - 1]:
                tmp2 = dp[index_b] * b
            if dp[index_c] * c != dp[i - 1]:
                tmp3 = dp[index_c] * c

            dp[i] = min(tmp1, tmp2, tmp3)

            if dp[i] == tmp1:
                index_a += 1
            if dp[i] == tmp2:
                index_b += 1
            if dp[i] == tmp3:
                index_c += 1

        return dp[n]


class Solution2:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        left = 1
        right = 1000000000 * 2
        ab = math.lcm(a, b)
        ac = math.lcm(a, c)
        bc = math.lcm(b, c)
        abc = math.lcm(a, bc)

        while left < right:
            mid = left + (right - left) // 2
            key = mid // a + mid // b + mid // c - mid // ab - mid // ac - mid // bc + mid // abc
            if key >= n:
                right = mid
            else:
                left = mid + 1

        return left


"""
Input: n = 3, a = 2, b = 3, c = 5
Output: 4
Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3rd is 4.

Input: n = 4, a = 2, b = 3, c = 4
Output: 6
Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4th is 6.

Input: n = 5, a = 2, b = 11, c = 13
Output: 10
Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5th is 10.

 *** 這題 Approach 1 答案是錯的 ***
 要再看過!!!!!
 
Approach 2: <Binary Search> HuaHua
為什麼想到是 Binary Search 呢？ => 因為我們看數據的規模非常的大, 所以我們如果要過測資, 
只能選擇 Time Complexity 為 O(1) or O(logn) 的方式,因此我們想到 binary search !!

Time Complexity: O(log(2^32)) = O(1)
Space Complexity: O(1)

這一題思路很神奇, 我們這裡要讓我們的 key 值變成我們的 n 值, 然後再找的這個過程是藉由 binary search 的特性下去做
"""

if __name__ == '__main__':
    demo2 = Solution2()
    print(demo2.nthUglyNumber(4, 2, 3, 4))
    print(demo2.nthUglyNumber(5, 2, 11, 13))
