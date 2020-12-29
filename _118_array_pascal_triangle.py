from typing import List


class Solution:

    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            res.append([])
            for j in range(i + 1):
                if j in (0, i):  # 表示j == 0 or j == i 的時候(即頭跟尾)
                    res[i].append(1)
                else:
                    res[i].append(res[i - 1][j - 1] + res[i - 1][j])

        return res


class Solution2:
    def generate(self, num_rows):
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle


"""

    Approach 1: DP Michelle
    Input: 5
    Output:
    [
         [1],
        [1,1],
       [1,2,1],
      [1,3,3,1],
     [1,4,6,4,1]
    ]
    TIME COMPLEXITY: O(N^2) / SPACE COMPLEXITY:O(N^2) (1+...+N)(我不確定)
    https://www.youtube.com/watch?v=gq4t3cwMQbs
    
    2020 / 12 / 28, updated
    Approach 2: DP
    
    Time Complexity: O( numRows^2 )
    Space Complexity: O( numRows^2 )
"""

if __name__ == '__main__':
    demo = Solution()
    res = demo.generate(5)
    print(res)
