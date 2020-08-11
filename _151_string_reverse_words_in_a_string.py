class Solution:
    def reverseWords(self, s: str) -> str:
        if s == "":
            return s

        ls = s.split()
        if ls == []:
            return ""

        res = ""

        for i in range(0, len(ls) - 1):
            res += ls[len(ls) - 1 - i] + " "
        res += ls[0]

        return res


""" 
    Input: "  hello world!  "
    Output: "world! hello"
    Explanation: Your reversed string should not contain leading or trailing spaces.
    
    https://www.youtube.com/watch?v=T3Sz-SI3gVE
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "the sky is blue"
    print(demo.reverseWords(input_1))
