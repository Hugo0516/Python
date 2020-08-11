from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        reach = 0
        for i, num in enumerate(nums):
            if i > reach:
                return False
            reach = max(reach, i + num)
        return True


"""
    這個題的tag是貪心，貪心策略是我們每次都選取最優的策略，然後前面已經選好了的就不用管了。

    這個題的貪心方法是，我們使用一個變量reach保存當前能到達的最後位置索引，那麼在每個位置的時候判斷這個位置能不能到達，
    即位置的索引大於了reach說明前面無論怎麼走也走不到這個位置，就返回False好了。如果這個位置可以到達，那麼要維護一下這個reach，
    更新策略是當前位置索引+這個數字代表的能向右走多少步，這個代表了到達當前位置的時候向右能到達的最遠距離，在這個最遠距離以內的任何位置都能到，
    因為每次跳的步數可以變小的。那麼進行了這麼一次循環以後，每個位置都判斷為能到達，所以結果返回True就好了。


    貪心和DP的比較：

    貪心算法（又稱貪婪算法）是指，在對問題求解時，總是做出在當前看來最好的選擇。也就是說，不從整體最優上加以考慮，
    他所作出的是在某種意義上的局部最優解。貪心算法和動態規划算法都是由局部最優導出全局最優，這裡不得不比較下二者的區別。

    貪心算法：
    1.貪心算法中，作出的每步貪心決策都無法改變，因為貪心策略是由上一步的最優解推導下一步的最優解，而上一步之前的最優解則不作保留；
    2.由（ 1）中的介紹，可以知道貪心法正確的條件是：每一步的最優解一定包含上一步的最優解。
    
    動態規划算法：
    1.全局最優解中一定包含某个局部最优解，但不一定包含前一個局部最優解，因此需要記錄之前的所有最优解；
    2.動態規劃的關鍵是狀態轉移方程，即如何由以求出的局部最優解來推導全局最優解；
    3.邊界條件：即最簡單的，可以直接得出的局部最優解。
    
    Time Complexity: O(N) / Space Complexity: O(1)
    https://blog.csdn.net/fuxuemingzhu/java/article/details/83504437
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [2, 3, 1, 1, 4]
    print(demo.canJump(input_1))
