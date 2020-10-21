import collections


class Solution:
    def firstUniqChar(self, s: str) -> int:
        # build hash map : character and how often it appears
        count = collections.Counter(s)

        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx
        return -1


"""
    s = "leetcode"
    return 0.

    s = "loveleetcode"
    return 2.
    
    Time complexity : O(N) since we go through the string of length N two times
    Space complexity : O(1) because English alphabet contains 26 letters.
    Space Complexity = O(1) 因為 key 最多只有26個, 每個value of key 只有一位, 所以頂多加起來 52
    因為是已知常數, 所以我們說他為 O(1) 
"""

if __name__ == '__main__':
    demo = Solution()
    demo.firstUniqChar("leetcode")
