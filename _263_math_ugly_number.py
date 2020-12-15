class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False

        factors = [2, 3, 5]

        for factor in factors:
            while num % factor == 0:
                num /= factor

        return num == 1


"""
Input: 6
Output: true
Explanation: 6 = 2 × 3

Input: 14
Output: false 
Explanation: 14 is not ugly since it includes another prime factor 7.

這一題的想法來在於： num = p1^k1 * p2^k2 * p3^k3....
p1, p2, p3, ..... => 都是 prime

=> 任一個數可以表示為質數的乘積

Time Complexity: O( log(2)n + log(3)n + log(5)n )
Space Complexity: O(1)
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.isUgly(6))
    print(demo.isUgly(14))
    print(demo.isUgly(8))
