from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        if image[sr][sc] == newColor:
            return image
        m = len(image)
        n = len(image[0])

        self._dfs(image, sc, sr, n, m, image[sr][sc], newColor)
        return image

    def _dfs(self, image, x, y, n, m, orgColor, newColor):

        if x < 0 or x >= n or y < 0 or y >= m:
            return
        if image[y][x] != orgColor:
            return

        image[y][x] = newColor
        self._dfs(image, x + 1, y, n, m, orgColor, newColor)
        self._dfs(image, x - 1, y, n, m, orgColor, newColor)
        self._dfs(image, x, y + 1, n, m, orgColor, newColor)
        self._dfs(image, x, y - 1, n, m, orgColor, newColor)


"""
    Reference: Hua Hua
    
    Why use DFS, 無相圖找連通分量, 和 695. Max area of Island, 200. Number of Island!!!, 547. Friend Cycle
    
    Time Complexity: O(N)
    Space Complexity: O(N)
    
"""

demo = Solution()
