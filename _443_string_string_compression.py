from typing import List


class Solution(object):
    def compress(self, chars: List[str]):
        anchor = write = 0
        for read, c in enumerate(chars):
            if read + 1 == len(chars) or chars[read + 1] != c:
                chars[write] = chars[anchor]
                write += 1
                if read > anchor:
                    for digit in str(read - anchor + 1):
                        chars[write] = digit
                        write += 1
                anchor = read + 1
        return write


class Solution2:
    def compress(self, chars: List[str]):
        n = len(chars)
        i, count = 0, 1

        for j in range(1, n + 1):
            if j < n and chars[j] == chars[j - 1]:
                count += 1
            else:
                chars[i] = chars[j - 1]
                i += 1
                if count > 1:
                    for digit in str(count):
                        chars[i] = digit
                        i += 1
                count = 1

        return i


"""
We will use separate pointers read and write to mark where we are reading and writing from. 
Both operations will be done left to right alternately: we will read a contiguous group of characters, 
then write the compressed version to the array. 

At the end, the position of the write head will be the length of the answer that was written.

input ["a","a","b","b","a","a","a"] and ["a","2","b","2","a","3"] as output.
 
Time Complexity: O(N)
Space Complexity: O(1)

Approach 1: Leetcode
Approach 2: Michelle
=> 觀念都一樣
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = ["a", "a", "b", "b", "a", "a", "a"]
    demo.compress(input_1)
    print(input_1)

    demo2 = Solution2()
    input_2 = ["a", "a", "b", "b", "a", "a", "a"]
    demo2.compress(input_2)
    print(input_2)

    input_3 = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
    demo2.compress(input_3)
    print(input_3)
