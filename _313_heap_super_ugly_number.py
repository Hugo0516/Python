from heapq import heappop, heappush
from typing import List


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        h, heap = set([1]), [1]
        while n:
            a = heappop(heap)
            for i in primes:
                m = a * i
                if not m in h:
                    heappush(heap, m)
                    h.add(m)
            n -= 1
        return a


"""
Input: n = 12, primes = [2,7,13,19]
Output: 32 
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12 
             super ugly numbers given primes = [2,7,13,19] of size 4.
             
For python heap library, heap push and pop are both O(logn)
Time Complexity: O(nlogn)
Space Complexity:O(n)

Reference: https://leetcode.com/problems/super-ugly-number/discuss/234588/Easy-python-solution-use-heap
我覺得解法蠻有趣的
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.nthSuperUglyNumber(12, [2, 7, 13, 19]))
