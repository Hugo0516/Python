import collections
import sys


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build the counter
        d = dict(collections.Counter(t))  # {'A':1, 'B':1, 'C':1}

        formed = 0  # 表示t 目前有幾位符合要求了
        left = 0  # 左邊界
        min_str = None
        min_length = sys.maxsize - 1

        for right in range(len(s)):  # 雖然右邊界叫 right, 但我們用for 一次只讓他動一格
            # skip, if s[right] doesn't matter
            ch = s[right]
            # right += 1
            if ch not in d:
                continue

            # use the ch to update d
            d[ch] -= 1
            if d[ch] == 0:
                formed += 1

            # if all characters are satisfied, then need to move the left pointer
            while formed == len(d) and left <= right:
                # save the result
                curr_length = right - left + 1
                if curr_length < min_length:
                    min_length = curr_length
                    min_str = s[left:right + 1]

                # update left boundary
                ch = s[left]
                left += 1
                if ch not in d:
                    continue
                d[ch] += 1
                if d[ch] == 1:
                    formed -= 1

        return min_str if min_str is not None else ""

    def minWindow2(self, s: str, t: str) -> str:
        # Input: S = "ADOBECODEBANC", T = "ABC"
        # Output: "BANC"
        # {'A':1, 'B':1, 'C':1}
        dict_1 = dict(collections.Counter(s))

        match = 0
        left = 0
        min_length = sys.maxsize - 1
        sub_str = ''

        for right in range(len(s)):
            ch = s[right]

            if ch not in dict_1:
                continue

            dict_1[ch] -= 1
            if dict_1[ch] == 0:
                match += 1

            while match == len(t) and left < right:
                # temp = min(temp, right - left + 1)
                # sub_str = s[left:right + 1]
                # 這兩行會錯, 是因為我原本設想進來這裡一次之後，再進到這裡來的都會比之前小,
                # 但是其實如果外面 for loop 跑了很多次, 可能 68行會維持 temp 而不是 right-left+1

                curr_length = right - left + 1
                if curr_length < min_length:
                    min_length = curr_length
                    sub_str = s[left:right + 1]
                    #  這個才符合邏輯

                ch = s[left]
                left += 1   # 這一行一定要寫在 81 之前
                if not ch in dict_1:
                    continue

                dict_1[ch] += 1
                if dict_1[ch] == 1:
                    match -= 1

        return sub_str


if __name__ == '__main__':
    demo = Solution()
    S = "AABNC"
    T = "AABC"
    print(demo.minWindow2(S, T))

"""
    Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
    Input: S = "ADOBECODEBAANC", T = "ABC"
    Output: "BAANC"
    
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
