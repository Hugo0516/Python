import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build the counter
        d = dict(collections.Counter(t))  # {'A':1, 'B':1, 'C':1}

        formed = 0  # 表示t 目前有幾位符合要求了
        slow = 0
        min_str = None
        min_length = sys.maxsize - 1

        for fast in range(len(s)):
            # skip, if s[fast] doesn't matter
            ch = s[fast]
            # fast += 1
            if ch not in d:
                continue

            # use the ch to update d
            d[ch] -= 1
            if d[ch] == 0:
                formed += 1

            # if all characters are satisfied, then need to move the left pointer
            while formed == len(d) and slow <= fast:
                # save the result
                curr_length = fast - slow + 1
                if curr_length < min_length:
                    min_length = curr_length
                    min_str = s[slow:fast+1]

                # update left boundary
                ch = s[slow]
                slow += 1
                if ch not in d:
                    continue
                d[ch] += 1
                if d[ch] == 1:
                    formed -= 1

        return min_str if min_str is not None else ""


if __name__ == '__main__':
    demo = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    print(demo.minWindow(S, T))

"""
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"
    
    看到str題目，又看到題目要求 Time Complexity = O(n), 
    自然而然就要想到 sliding window(利用two pointer技巧的一種方式, 左右邊會有fast/ slow pointer,視題目情況,看哪邊要fast 哪邊要slow)
    sliding window 題型：
    看到 minimun substr 這種類型的題目,為了使結果最小, 每次右邊界向右移動一格, 左邊界每次向右as much as possible,
    這樣可以使 s[slow:fast]中的substr最小
    (所以這樣的話, 右邊界可以用for, 左邊界可以用while)
    
    看到 maximum substr: 跟上面相反....
    
    Time Complexity: O(n)/ Space Complexity: O(n)
    https://www.youtube.com/watch?v=YP3bBDuojqk&t=32s
"""
