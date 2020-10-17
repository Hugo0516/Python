class Solution:
    # Hua Hua solution
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = [-1] * 128  # 理論上最長的不重複字符 = 128, Space Complexity: O(128)
        result = 0
        start = 0
        for i, ch in enumerate(s):  # take O(n) times to check
            if last[ord(ch)] != -1:  # ord 函數，可以返回 char 的 ASCII code
                start = max(start, last[ord(ch)] + 1)
            result = max(result, i - start + 1)
            last[ord(ch)] = i
        return result

    # Brute Force, Time Complexity:O(n^3), Space Complexity:O(k), k is size of set
    def lengthOfLongestSubstring2(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                if self.allUnique(s, i, j):
                    ans = max(ans, j - i)
        return ans

    # Brute Force
    def allUnique(self, s: str, start: int, end: int):
        temp = set()
        for i in range(start, end):
            char = s[i]
            if char in temp:
                return False
            temp.add(char)
        return True

    # Sliding Window, Time Complexity:O(2n), Space Complexity:(k), k is size of set
    # Remember this is okay
    def lengthOfLongestSubstring3(self, s: str) -> int:
        set_1 = set()
        start, end, ans = 0, 0, 0
        while start < len(s) and end < len(s):
            if s[end] not in set_1:
                set_1.add(s[end])
                end += 1
                ans = max(ans, end - start)
            else:
                set_1.remove(s[start])
                start += 1
        return ans


"""
    A sliding window is an abstract concept commonly used in array/string problems. 
    A window is a range of elements in the array/string which usually defined by the start and end indices, 
    i.e. [i,j) (left-closed, right-open). 
    A sliding window is a window "slides" its two boundaries to the certain direction. 
    For example, if we slide [i,j) to the right by 1 element, then it becomes [i+1,j+1) (left-closed, right-open).
    
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
    input_1 = "pwwkew"  # output = 3, (wke)
    input_2 = 'abcabcbb'
    print(demo.lengthOfLongestSubstring(input_1))

    print(demo.lengthOfLongestSubstring2(input_1))  # Brute Force

    print(demo.lengthOfLongestSubstring3(input_2))  # Remember this is okay
