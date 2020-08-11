class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len(num) == k:
            return '0'
        stack = []
        for n in num:
            while stack and k and int(stack[-1]) > int(n):
                stack.pop()
                k -= 1
            stack.append(n)
        while k:
            stack.pop()
            k -= 1
        if not stack:
            return '0'
        return str(int("".join(stack)))
        # str("".join(stack)) 的輸出為 0200
        # 所以先轉成 int 變成 200 再變成 str "200"

"""
    Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.
    Input: num = "1432219", k = 3
    Output: "1219"
    Explanation: Remove the three digits 4, 3, and 2 to form the new number 1219 which is the smallest.
    
    看到這種 K 相關的題目就要想到 stack !!!!!!
    EX: 378 
    
    要注意 join 的用法 

    t.ly/BQJq    
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "1432219"
    input_2 = "10200"
    input_3 = "10"
    print(demo.removeKdigits(input_1, 3))
    print(demo.removeKdigits(input_2, 1))
    print(demo.removeKdigits(input_3, 2))
