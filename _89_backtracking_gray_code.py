from typing import List


class Solution:
    def grayCode(self, n: int) -> List[int]:
        grays = dict()
        grays[0] = ['0']
        grays[1] = ['0', '1']
        for i in range(2, n + 1):
            n_gray = []
            for pre in grays[i - 1]:
                n_gray.append('0' + pre)
            for pre in grays[i - 1][::-1]:
                n_gray.append('1' + pre)
            grays[i] = n_gray
        return map(lambda x: int(x, 2), grays[n])

    def grayCode2(self, n):
        ans = [0]
        for i in range(n):
            for j in range(len(ans) - 1, -1, -1):
                print(i | ans[j], 1 << i | ans[j], sep=' ', end='\n')
                ans.append(1 << i | ans[j])
        return ans


class Solution2:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = self.grayCode(n - 1)
        num = 2 ** (n - 1)
        res += res[::-1]
        for i in range(num, len(res)):
            res[i] ^= num
        return res


"""
https://leetcode.com/problems/gray-code/discuss/216001/Python-solution

Time Complexity: O(2^n)
Space Complexity: O(2^n)

這題只能硬背 !!!!!!!!!!

看 Solution2, 然後這題沒有用到 backtracking 的解法 
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = 3
    output_1 = demo.grayCode2(input_1)
    print(output_1)

    print(1 << 1)

    demo2 = Solution2()
    output_2 = demo2.grayCode(input_1)
    print(output_2)
