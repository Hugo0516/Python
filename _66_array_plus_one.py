from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        N = len(digits)
        pos = N - 1
        carry = 0
        digits[-1] += 1
        while pos >= 0:
            digits[pos] += carry
            if digits[pos] >= 10:
                carry = 1
                digits[pos] -= 10
            else:
                carry = 0
            pos -= 1
        if carry:
            digits.insert(0, 1)
        return digits

"""
    使用carry表示進位，這樣我們把每個位置更新成當前的數字+carry即可，如果大於等於10，
    那麼carry就又是1，否則carry就是0了。這個操作很類似大整數加法。
    因為只有+1的操作，所以我在剛開始的時候，就對最後一個元素做了+1運算，這樣再次循環判斷是不是要進位即可。
    
    https://blog.csdn.net/fuxuemingzhu/java/article/details/51346096
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [1, 2, 3]
    input_2 = [4, 3, 2, 1]
    input_3 = [9, 9, 9]

    print(demo.plusOne(input_1))
    print(demo.plusOne(input_2))
    print(demo.plusOne(input_3))