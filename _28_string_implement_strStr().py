class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1

"""
    https://www.youtube.com/watch?v=62lXzTIHTiI
"""

if __name__ == '__main__':
    demo = Solution()
    haystack = "hello"
    needle = "ll"
    print(demo.strStr(haystack, needle))
