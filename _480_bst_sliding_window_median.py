from typing import List
import bisect


class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if k == 0:
            return []
        ans = []
        window = sorted(nums[0:k])

        for i in range(k, len(nums) + 1):
            # get median, 這方法 奇偶都適合
            ans.append((window[k // 2] + window[(k - 1) // 2]) / 2.0)
            if i == len(nums):
                break
            index = bisect.bisect_left(window, nums[i - k])
            # bisect 就相當於 binary search, 可以用低時間複雜度找到元素
            # 竟然提到 binary search 的話, 那你應該要知道：同樣的, 對 bisect 而言你必須給他 sorted list
            window.pop(index)
            # 移走最前面的元素
            bisect.insort_left(window, nums[i])
            # 後面新的元素補上來
        return ans


"""
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6

解題思路：這題和 239 類似, 這題看題目好像不難, 但是, 這題一開始你要想說, 我要怎麼樣的 operations 才可以讓我整體的時間複雜度降低
我要用什麼數據結構來優化過程 等等...
Reference: Hua Hua

Time Complexity: O( n-k+1 )*k, k的由來是因為 bisect=>logk, pop=>k, 所以 logk+k = k
Space Complexity: O(k), 因為要維持數組(k個數字)
"""
if __name__ == '__main__':
    demo = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    output_1 = demo.medianSlidingWindow(nums, k)
    print(output_1)
