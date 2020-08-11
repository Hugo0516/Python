from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        reach = 0
        cur = 0     # 當前這一步, 能到達的位置
        N = len(nums)
        count = 0       # 總共走幾步
        pos = 0
        while cur < N - 1:
            count += 1
            pre = cur   # pre = 上一次能到達的最遠位置
            while pos <= pre:
                cur = max(cur, pos + nums[pos])
                pos += 1
        return count

"""
    這個題和55. Jump Game很像，都是求怎麼能跳到最後的位置，只不過這個題加了一個條件，就是我們需要的最小的步數，使用的策略是貪心。

    我們每次貪心的找在自己當前能到達的幾個位置裡面，跳到哪個位置的時候，在下一步能跳的最遠。
    然後，我們當前步就跳到這個位置上去，所以我們在這一步的跳躍時，給下一步留下了最好的結果。

    所以，使用一個cur表示當前步能到達的最遠位置，使用pre表示上一次能到達的最遠位置。
    所以，我們應該遍歷在上一步的覆蓋範圍內，當前能跳的最遠位置來更新cur。一個節省計算資源的方式是，保存以前已經檢查了的位置為Pos，這樣每次檢查的範圍是pos~pre。

    https://blog.csdn.net/fuxuemingzhu/java/article/details/84578893
"""

if __name__ == '__main__':

    demo = Solution()
    input_1 = [2, 3, 1, 1, 4]
    print(demo.jump(input_1))