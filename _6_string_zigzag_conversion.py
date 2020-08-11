class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s
        list_1 = [[] for i in range(numRows)]

        for i in range(len(s)):
            index = i % (2*numRows-2)
            index = index if index < numRows else 2*numRows-2-index # 像是 index[1]的第二個 P 因為 index < numRows
            # 所以必須想到 2*numRows-2-index
            list_1[index] += s[i]

        for i in range(1, len(list_1)):
            list_1[0] += list_1[i]

        return ''.join(list_1[0])

"""
    解題思路：
            Input: s = "PAYPALISHIRING", numRows = 3 / Output: "PAHN, APLSIIG, YIR"(ignore comma and space)
            index[0]    P   A   H   N
            index[1]    A P L S I I G   將PAYP 看成一個 V 形狀
            index[2]    Y   I   R
            
            Time Complexity: O(n) / Space Complexity: O(n)(因為 list_1 大小為n)
            *** join 的用法 是將序列造我們訂的規則變成我們想要的字符串
            https://www.youtube.com/watch?v=NfBcHxRe8jo
"""

if __name__ == '__main__':
    demo = Solution()
    input_s = "PAYPALISHIRING"
    input_num = 3
    print(demo.convert(input_s,input_num))