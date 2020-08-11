class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        def getLen(l, r):   # 就是拿來算 palindrome 有多長的算法, l = left, r = right
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1    # 因為 l -= 1, r += 1 所以會超出有回文的長度 = r - l + 1 - 2

        start = 0
        length = 0
        for i in range(n):
            cur = max(getLen(i, i), # s 是 odd
                      getLen(i, i + 1)) # s 是 even
            if cur <= length: continue  # 如果這次的 cur > 之前所存的最大 length 想當然耳取代之前的 length
            length = cur
            start = i - (cur - 1) // 2  # // 代表整數除法, / 代表除法
        return s[start: start + length]

"""
解題思路：
        if s[i~j] is a palindrome, s[i+1 ~ j-1] is also a one.
        if s[i~j] is not a palindrome, then s[i-1 ~ j+1] can not be a palindrome.
        e.g. abcea, bce is not a palindrome, abcea can't be one.
        Instead of starting from two sides, we can start from the center. 
        For each index i, or pair (i, i+1) we take it as the middle elements and expand towards two ends to find the longest palindrome.
        Time complexity: best O(n), worst O(n^2)
        Space complexity: O(1)
        
        這題用從中間往兩旁邊擴展的想法去想
        
        Input: "babad"
        Output: "bab"
        Note: "aba" is also a valid answer.
        
        https://www.youtube.com/watch?v=g3R-pjUNa3k
"""

# class Solution(object):
#     def longestPalindrome(self, s):
#         """
#         :type s: str
#         :rtype: str
#         """
#         if len(set(s)) == 1: return s
#         n = len(s)
#         start, end, maxL = 0, 0, 0
#         dp = [[0] * n for _ in range(n)]
#         for i in range(n):
#             for j in range(i):
#                 dp[j][i] = (s[j] == s[i]) & ((i - j < 2) | dp[j + 1][i - 1])
#                 if dp[j][i] and maxL < i - j + 1:
#                     maxL = i - j + 1
#                     start = j
#                     end = i
#             dp[i][i] = 1
#         return s[start: end + 1]
"""
解題思路：
        動態規劃的兩個特點：第一大問題拆解為小問題，第二重複利用之前的計算結果，來解答這道題。

        那如何劃分小問題呢，我們可以先把所有長度最短為1的子字符串計算出來，根據起始位置從左向右，這些必定是回文。
        然後計算所有長度為2的子字符串，再根據起始位置從左向右。到長度為3的時候，我們就可以利用上次的計算結果：
        如果中心對稱的短字符串不是回文，那長字符串也不是，如果短字符串是回文，那就要看長字符串兩頭是否一樣。
        這樣，一直到長度最大的子字符串，我們就把整個字符串集窮舉完了。

        我們維護一個二維數組dp，其中dp[i][j]表示字符串區間[i, j]是否為回文串，當i = j時，只有一個字符，肯定是回文串，
        如果i = j + 1，說明是相鄰字符，此時需要判斷s[i]是否等於s[j]，如果i和j不相鄰，即i - j >= 2時，
        除了判斷s[i]和s [j]相等之外，dp[j + 1][i - 1]若為真，就是回文串，通過以上分析，可以寫出遞推式如下：
        dp[i, j] = 1    if i == j
                 = s[i] == s[j]     if j = i + 1
                 = s[i] == s[j] && dp[i+1][j-1]     if j > i + 1
https://blog.csdn.net/fuxuemingzhu/java/article/details/79573621
這方法比較慢，我也沒仔細看，可是好像是標準dp?
"""


def main():
    demo = Solution()
    print(demo.longestPalindrome('abcbaa'))


if __name__ == '__main__':
    main()
