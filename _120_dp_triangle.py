from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        length = len(triangle)  # length = 4
        dp = [0] * (length + 1)  # (0-4)

        for i in range(length - 1, -1, -1):  # (3-0)
            for j in range(i + 1):  # (0-3)
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]

        return dp[0]


"""
        When we saw key words: minimum => think about greedy strategy or dynamic programming
        => apparently, here we have to choose dynamic programming
        
        dp題目 可以從起始看到結尾推出來, 或是像這一題一樣從結尾推回起始!!!!

        這題要注意, row 跟 column 都為1~4, 但是裡面List的起始位置為0 !!!
        dp[i] = curVal + min(dp[i], dp[i+1])
        
                    dp[0]
                  dp[0]dp[1]
               dp[0]dp[1]dp[2]
             dp[0]dp[1]dp[2]dp[3]   (實際上從這層開始)(因為就算從這層開始也要符合條件(即: dp[i]=curVal+min(dp[i],dp[i+1])) (所以下面的幻想要有5格)(這也是為什麼#7要length+1)
           dp[0]dp[1]dp[2]dp[3]dp[4] (這層是幻想的)     (#25的 dp[3] = min(dp[3],dp[4])+curVal)
           
        這題的解法還符合 O(n) extra space 的解法
        https://www.youtube.com/watch?v=p1LlPZYw42g
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(demo.minimumTotal(input_1))

    input_2 = [[-1], [2, 3], [1, -1, -3]]
    print(demo.minimumTotal(input_2))
