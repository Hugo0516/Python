class Solution:
    # hashmap version:
    def lengthOfLongestSubstringTwoDistinct(self, s: str)-> int:
        if not s: return 0
        window = dict()
        max_len = 0
        l = -1  # 一切都是為了 max-len的問題

        for r, char in enumerate(s):  # O(N)
            window[char] = r
            if len(window) > 2:
                l = min(window.values())  # O(k)
                window.pop(s[l])
            max_len = max(max_len, r - l)

        return max_len

    # def lengthOfLongestSubstringTwoDistinct2(self, s: str)-> int:




if __name__ == '__main__':
    demo = Solution()
    s1 = "eceba"
    k1 = 2
    s2 = "aa"
    k2 = 1
    print(demo.lengthOfLongestSubstringTwoDistinct(s1))

"""
給定字符串s，找到包含最多2個不同字符的最長子字符串t  的長度  。

範例1：

輸入：“ eceba”
輸出3
說明：t是“ ece”，其長度為3。
範例2：

輸入：“ ccaabbb”
輸出：5
說明：t是“ aabbb”，其長度為5。

這是我參考340, 所改寫的, 好像用 sliding window 比較麻煩, 不過可以try 一下
"""