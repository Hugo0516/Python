class Solution:
    def __init__(self):
        self.dp = dict()

    def numTrees(self, n: int) -> int:  # recursion + cache 方法
        if n == 0 or n == 1:
            return 1
        if n in self.dp:
            return self.dp[n]

        ans = 0
        for i in range(1, n + 1):
            ans += self.numTrees(i - 1) * self.numTrees(n - i)  # 若是改成 i 和 n-i-1 會錯(因為n-i-1會變負的)
            # (l: 0, 1, 2; r: 2, 1, 0)!!!!!!!!!!!!!!!!!!!! 和 No.894性質有差
        self.dp[n] = ans

        return ans

    def numTrees2(self, n: int) -> int:  # DP 方法
        if n < 1:
            return 1  # 19, 20 行 好像可有可無

        res = [0 for i in range(n + 1)]
        res[0] = res[1] = 1

        for i in range(2, n + 1):
            for j in range(0, i):
                res[i] += res[i - j - 1] * res[j]

        return res[n]


class Solution2:
    def numTrees(self, n: int) -> int:

        G = [0] * (n + 1)
        G[0], G[1] = 1, 1

        for i in range(2, n + 1):
            for j in range(1, i + 1):
                G[i] += G[j - 1] * G[i - j]

        return G[n]


class Solution3(object):
    def numTrees(self, n):
        C = 1
        for i in range(0, n):
            C = C * 2 * (2 * i + 1) / (i + 2)
        return int(C)


"""
    解題思路：
            方法一: 56ms
            https://blog.csdn.net/fuxuemingzhu/article/details/79367789
            (這recursion方法, 可以協助我們做95題)
            思路：從1...n中找出一個i作為根節點，比i小的數1...i-1作為左子樹，比i大的數i+1...n作為右子樹，左子樹的排列和右子樹的排列的乘積是此時的數目。
            
            方法二: 28ms 
            方法二的速度比較快!!
            https://www.youtube.com/watch?v=HWJEMKWzy-Q
            
            Time Complexity: O(n + n^2/2) = O(n^2)(我猜啦)
            Space Complexity: O(n)
            
            其實這一題是卡特蘭函數的應用題目：
            https://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0

2020 / 12 / 29 updated
Approach 2: Dynamic Programming

Time Complexity: O(N^2)
Space Complexity: O(N)

G(n): the number of unique BST for a sequence of length n. => G is a Catalan number !!!!!!!!
F(i,n): the number of unique BST, where the number i is served as the root of BST (1 ≤ i ≤ n).

Relationship:
=> G(n) = ∑(i=1 to n)F(i,n) => G(0) = 1, G(1) = 1
=> F(i,n) = G(i-1) * G(n-i)
=> G(n) = ∑(i=1 to n) G(i-1) * G(n-i)

Approach 3: Catalan number

Time Complexity: O(N), as one can see, there is one single loop in the algorithm.
Space Complexity: O(1), we use only one variable to store all the intermediate results and the final one.
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.numTrees(3))
    print(demo.numTrees2(3))

    demo2 = Solution2()
    print(demo2.numTrees(3))
