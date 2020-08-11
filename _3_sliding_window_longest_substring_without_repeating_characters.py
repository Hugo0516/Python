class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128   # 理論上最長的不重複字符 = 128, Space Complexity: O(128)
        result = 0
        start = 0
        for i, ch in enumerate(s):  # take O(n) times to check
            if last[ord(ch)] != -1:  # ord 函數，可以返回 char 的 ASCII code
                start = max(start, last[ord(ch)] + 1)
            result = max(result, i - start + 1)
            last[ord(ch)] = i
        return result


"""
    解題思路：
            Common sense: 長度為n的字串，可以被分割成總共： 1+....+n + 1(空字串) = (1+n)*n/2 +1 = O(n^2)
            Sliding window 的意思是說，其實就是想一下，我們就像是用一個會滑動的 window 在選取我們的 substring
            Window (i, j) with unique characters
            1. use a hashtable to store the last indies of each characters
            2. keep track the valid starting point 
                a. when there is a match update the string point to the current one
            i = max(i, m[s[j]] + 1), len = j - i + 1
            
            Brute force: Time Complexity: O(n^3) =>  O(n * 128^2)
            
            Time Complexity: O(n) / Space Complexity: O(128) (因爲ASCII碼，共128個(0 ~ 127))
            
            Input: "pwwkew"
            Output: 3
            Explanation: The answer is "wke", with the length of 3. 
            Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
            https://www.youtube.com/watch?v=LupZFfCCbAU
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "pwwkew"
    print(demo.lengthOfLongestSubstring(input_1))