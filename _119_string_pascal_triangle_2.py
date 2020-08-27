from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1] + [0] * rowIndex

        for i in range(rowIndex):
            # res[0] = 1
            for j in range(i + 1, 0, -1):   # 一樣是包含頭不包含尾
                res[j] = res[j] + res[j - 1]

        return res


class Solution2:

    def getRow2(self, rowIndex: int) -> List[int]:
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


"""
    Input: rowIndex = 3
    Output: [1,3,3,1]
    
    Solution 的解法才能達到 TIME COMPLEXITY = O(K) 的程度
    某個低能兒提供的Solution2 解法還是一樣O(k^2) 真的白痴
    Solution才是正確的！
    
    https://www.youtube.com/watch?v=PKiV5HhnfDw
    
    Steps:
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
