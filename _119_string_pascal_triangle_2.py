from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] + [0] * rowIndex

        for i in range(rowIndex):
            # res[0] = 1
            for j in range(i + 1, 0, -1):  # 一樣是包含頭不包含尾
                res[j] = res[j] + res[j - 1]

        return res


class Solution2:

    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(rowIndex + 1):
            result.append([])
            for j in range(i + 1):
                if j == 0:
                    result[i].append(1)
                elif j == i:
                    result[i].append(1)
                else:
                    result[i].append(result[i - 1][j - 1] + result[i - 1][j])
        return result[rowIndex]


class Solution3:
    # 這是 top-down 的方法
    def getRow(self, rowIndex: int) -> List[int]:
        def getNum(row: int, col: int):
            if row == 0 or col == 0 or row == col:
                return 1
            return getNum(row - 1, col - 1) + getNum(row - 1, col)

        ans = []

        for i in range(rowIndex + 1):
            ans.append(getNum(rowIndex, i))

        return ans


class Solution4:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [[1 for i in range(rowIndex + 1)] for j in range(rowIndex + 1)]

        for i in range(rowIndex + 1):
            for j in range(rowIndex):
                if i == 0 or j == 0 or i == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]

        return dp[rowIndex]


class Solution5:
    def getRow(self, rowIndex: int) -> List[int]:
        dp = [1 for i in range(rowIndex + 1)]

        for i in range(rowIndex):
            j = i
            while i > 0:
                dp[j] = dp[j] + dp[j - 1]
            dp.append(1)

        return dp


"""    
    Reference:
    *** 記住第一個方法 ***
    Approach 1: Michelle
    Time Complexity: O(k^2)
    Space Complexity: O(1)
    
    Approach 2: Michelle 說明底下, 路人提供的解答
    Time Complexity: O(k^2)
    Space Complexity:  O(^2)
    
    Approach 3: Brute Force: => Time limit exceeded
    Time Complexity: O(2^k), T(k, i) = T(k-1, i) + T(k-1, i-1) + O(1)
    
    Space Complexity: O(k), we need O(k) space to store the output of the kth row.
    At worst, the recursive call stack has a maximum of k calls in memory,
    each call taking constant space. That's O(k) worst case recursive call stack space.
    
    Constraints:
    1. getNUm(row, col) = getNum(row-1, col-1) + getNum(row-1, col)
    2. The first row is just a single 1
    3. The first and last number of each rows is 1, getNum(k, 0) = getNum(k, k) = 1
    
    Approach 4: DP, I did it by myself
    *** 可以參考 ***
    Time Complexity: O(n^2)
    Space Complexity: O(n^2)
    

    
    Approach 1 Steps:
    i = 0
    j = 1
    [1, 1, 0, 0]
    
    i = 1
    j = 2
    [1, 1, 1, 0]
    i = 1
    j = 1
    [1, 2, 1, 0]
    
    i = 2
    j = 3
    [1, 2, 1, 1]
    i = 2
    j = 2
    [1, 2, 3, 1]
    i = 2
    j = 1
    [1, 3, 3, 1]
"""
if __name__ == '__main__':
    demo = Solution()
    print(demo.getRow(3))

    demo3 = Solution3()
    print(demo3.getRow(4))

    demo4 = Solution4()
    print(demo4.getRow(4))
