from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        visited = set()
        ans = 0
        n = len(M)

        def dfs(graph, node, n, visited):
            if node in visited:
                return
            visited.add(node)
            for i in range(n):
                if graph[node][i] and not i in visited:
                    dfs(graph, i, n, visited)

        for i in range(n):
            if i not in visited:
                dfs(M, i, n, visited)
                ans += 1  # 和 200很像
        return ans


class Solution2(object):
    def findCircleNum(self, M):

        def dfs(M, curr, n):
            for i in range(n):
                if M[curr][i] == 1:
                    M[curr][i] = M[i][curr] = 0
                    dfs(M, i, n)

        n = len(M)
        ans = 0
        for i in range(n):
            if M[i][i] == 1:
                ans += 1
                dfs(M, i, n)

        return ans


"""
    Input:
            [ [1,1,0],
              [1,1,0],
              [0,0,1] ]
      
    Output: 2
    
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
    The 2nd student himself is in a friend circle. So return 2.
    
    這一題可以用 DFS / Union Find 去解
    直覺會想到 DFS
    
    Time Complexity : O(n^2) / Space Complexity: O(n) (extra)
    用 Union Find 的話 Time Complexity可以降到 O(n) !!!!!!!
    
    這一題和 Leetcode 200 一樣的思路, 一樣會想到 connected component
    
    Method 1:是我自己想出來的
    
    Method 2：
    https://zxi.mytechroad.com/blog/graph/leetcode-547-friend-circles/
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]
    input_2 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]
    print(demo.findCircleNum(input_1))  # expect 2
    print(demo.findCircleNum(input_2))  # expect 3

    demo_2 = Solution2()
    input_1 = [[1, 1, 0],
               [1, 1, 0],
               [0, 0, 1]]
    input_2 = [[1, 0, 0],
               [0, 1, 0],
               [0, 0, 1]]
    print(demo_2.findCircleNum(input_1))
    print(demo_2.findCircleNum(input_2))
