from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        res = 0

        for i in range(len(triangle)):
            triangle[i].sort()
            res += triangle[i][0]

        return res


if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [2],
        [3, 4],
        [6, 5, 7],
        [4, 1, 8, 3]
    ]
    print(demo.minimumTotal(input_1))

    input_2 = [[-1], [2, 3], [1, -1, -3]]
    print(demo.minimumTotal(input_2))
