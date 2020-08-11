class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = 0
        a = abs(x)

        while(a != 0):
            temp = a % 10
            num = num * 10 + temp
            a = a // 10     # 如果這裡改成 int(a/10) 會變慢哦，要注意

        if x >= 0 and x == num:
            return True
        else:
            return False

"""
    解題思路：
            Follow up:
            Could you solve it without converting the integer to a string?
            這題跟第七題很像，如果這題用第七題的算法，可以計算的更快，但是題目的 follow up 不准
            
            https://www.youtube.com/watch?v=qv7yjO5V7I0
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = -123
    print(demo.isPalindrome(input_1))