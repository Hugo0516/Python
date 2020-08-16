from typing import List


class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:

        # def dfs(M, curr, n):
        #     for i in range(n):
        #         if M[curr][i] == 1:
        #             M[curr][i] = M[i][curr] = 0
        #             dfs(M, i, n)

        # n = len(M)
        # ans = 0
        # for i in range(n):
        #     if M[i][i] == 1:
        #         ans += 1
        #         dfs(M, i, n)
        #
        # return ans

        visited = set()
        connected_component = []

        def dfs(graph, node, visited, temp):
            temp.append(node)
            visited.add(node)
            for neightbor in graph[node]:
                if neightbor not in visited:
                    dfs(graph, neightbor, visited, temp)
            return temp

        for i in range(len(M)):
            if i not in visited:
                temp = []
                connected_component.append(dfs(M, i, visited, temp))

        # print(connected_component)
        return len(connected_component)

"""
    Input:
    [ [1,1,0],
      [1,1,0],
      [0,0,1] ]
    Output: 2
    Explanation:The 0th and 1st students are direct friends, so they are in a friend circle.
    The 2nd student himself is in a friend circle. So return 2.
    
    我覺得我寫的方法比較好
    
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

    # for row in input_1:
    #     for i in row:
    #         print(i, row)
