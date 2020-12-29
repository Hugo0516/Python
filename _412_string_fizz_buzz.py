from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append('FizzBuzz')
            elif i % 3 == 0:
                result.append('Fizz')
            elif i % 5 == 0:
                result.append('Buzz')
            else:
                result.append(str(i))

        return result


"""
Time Complexity: O(N)
Space Complexity: O(1)
"""
if __name__ == '__main__':
    demo = Solution()
    print(demo.fizzBuzz(15))
