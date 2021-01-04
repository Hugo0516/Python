from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [arr[0]]
        res = 0

        for i in range(1, len(arr)):
            while stack and arr[i] >= stack[-1]:
                top = stack.pop()
                if len(stack) == 0:
                    res += top * arr[i]
                else:
                    res += top * min(arr[i], stack[-1])

            stack.append(arr[i])

        while len(stack) > 1:
            res += stack.pop() * stack[-1]

        return res


"""
<這題有多種解法, DP, STACK, GREEDY.....> 我用了 stack 感覺比較好懂= =

STACK Reference:https://www.youtube.com/watch?v=abMfdlnCW5c

Time Complexity: 
Space Complexity: O(n)

DP REFERENCE: https://github.com/wisdompeak/LeetCode/tree/master/Dynamic_Programming/1130.Minimum-Cost-Tree-From-Leaf-Values


"""

if __name__ == '__main__':
    demo = Solution()
    arr = [6, 2, 4]
    arr2 = [15, 13, 5, 3, 12]

    print(demo.mctFromLeafValues(arr))
    print(demo.mctFromLeafValues(arr2))
