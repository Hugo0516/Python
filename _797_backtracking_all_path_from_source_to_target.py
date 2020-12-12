from collections import deque
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def backtrack(currNode, path):
            # if we reach the target, no need to explore further.
            if currNode == target:
                results.append(list(path))
                return
            # explore the neighbor nodes one after another.
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()

        # kick of the backtracking, starting from the source node (0).
        path = deque([0])
        backtrack(0, path)

        return results


"""
Input: [[1,2], [3], [3], []] 
Output: [[0,1,3],[0,2,3]] 

Explanation: The graph looks like this:

0--->1
|    |
v    v
2--->3

There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
給出了一個有向無環圖，求從起點到終點的所有路徑。圖的表示方法是，共有n個節點，其數字分別為0…n-1，
給出的圖graph的每個位置對應的是第i個節點能到達的下一個節點的序號位置。比如題中graph[0] = [1,2]表示圖的起點0指向了1,2兩個節點。

Let N be the number of nodes in the graph
Time Complexity: O( 2^N * N )
Space Complexity: O( 2^N * N )

請看 Leetcode 解釋, 這分析太難 = =
"""

if __name__ == '__main__':
    demo = Solution()
    graph = [[1, 2], [3], [3], []]
    print(demo.allPathsSourceTarget(graph))
