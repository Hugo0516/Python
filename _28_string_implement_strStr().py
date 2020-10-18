class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle is None:
            return 0

        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i: i + len(needle)] == needle:
                return i
        return -1


"""
    這題的重點應該在於, 我們不能用函示 ex indexOf 來偷吃步才對
    Clarification:

    What should we return when needle is an empty string? 
    This is a great question to ask during an interview.
    
    For the purpose of this problem, we will return 0 when needle is an empty string. 
    This is consistent to C's strstr() and Java's indexOf().
    
    https://www.youtube.com/watch?v=62lXzTIHTiI
"""

if __name__ == '__main__':
    demo = Solution()
    haystack = "hello"
    needle = "ll"
    print(demo.strStr(haystack, needle))
