from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        M, N = len(matrix), len(matrix[0])
        left, right, up, down = 0, N - 1, 0, M - 1
        res = []
        x, y = 0, 0
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_d = 0
        while len(res) != M * N:
            res.append(matrix[x][y])
            if cur_d == 0 and y == right:
                cur_d += 1
                up += 1
            elif cur_d == 1 and x == down:
                cur_d += 1
                right -= 1
            elif cur_d == 2 and y == left:
                cur_d += 1
                down -= 1
            elif cur_d == 3 and x == up:
                cur_d += 1
                left += 1
            cur_d %= 4
            x += dirs[cur_d][0]
            y += dirs[cur_d][1]
        return res

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []
        col = len(matrix[0])
        res = matrix[0]

        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col - 1])
            for j in range(col - 2, -1, -1):
                print(j)
                res.append(matrix[row - 1][j])
            if col > 1:
                for i in range(row - 2, 0, -1):
                    print(i)
                    res.append(matrix[i][0])

        M = []
        for k in range(1, row - 1):
            t = matrix[k][1:-1]
            M.append(t)

        return res + self.spiralOrder2(M)


"""
    method 1:
    https://blog.csdn.net/fuxuemingzhu/java/article/details/79541501
    
    method 2: (比較好!!!!!!!) (和 59 比較)!!!!
    Time Complexity: / Space Complexity: O(M*N*min(M,N)) (不確定)
    
    https://www.youtube.com/watch?v=cedA25UQWcA
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    input_2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]

    # print(demo.spiralOrder(input_1))
    # print(demo.spiralOrder(input_2))

    print(demo.spiralOrder2(input_2))
