inf = float('inf')
# 可以想有六個點，點從 1~6
matrix_distance = [[0, 1, 12, inf, inf, inf],
                   [inf, 0, 9, 3, inf, inf],
                   [inf, inf, 0, inf, 5, inf],
                   [inf, inf, 4, 0, 13, 15],
                   [inf, inf, inf, inf, 0, 4],
                   [inf, inf, inf, inf, inf, 0]]


def dijkstra(matrix_distance, source_node):
    inf = float('inf')
    # init the source node distance to others
    dis = matrix_distance[source_node]  # source node 到其他點的距離
    node_nums = len(dis)

    found = [0 for i in range(node_nums)]  # found[i] = 0 表示到i的最短距離還沒被找到
    found[source_node] = 1  # 我們的 source node 因為是起點，所以當然是 True

    for i in range(node_nums - 1):  # 扣除原點 還有五個點(即原點到那五個點的最短距離)
        min = inf  # 這一行很重要哦！！！ 算是 initiate step

        # find the min node from the source node
        # 25-29行, 是要先求出"一個"與 source node 最靠近的點, 即 u 點 (即 花費最少的邊)
        # 每次都選最短的(greedy), 然後再從最短的那裡延伸出去繼續搜索
        for j in range(node_nums):
            if found[j] == 0 and dis[j] < min:
                min = dis[j]
                u = j
        found[u] = 1

        # update the dis
        for v in range(node_nums):
            # found[v] == 0 表示起點到v的最佳解還沒找到(24-28行的任務) matrix[u][v]<inf 表示 u和v有連結
            if found[v] == 0 and matrix_distance[u][v] < inf:
                if dis[u] + matrix_distance[u][v] < dis[v]:  # dis[?] 被更新 所以 (24-28) 行才有好互相比較
                    dis[v] = dis[u] + matrix_distance[u][v]

    return dis


# 記住！！！ 1個for 包著 2個 for

print(dijkstra(matrix_distance, 0))
print('')


def Floyd(dis):  # (核心: DP)
    # min (Dis(i,j) , Dis(i,k) + Dis(k,j) )
    nums_vertex = len(dis[0])
    for k in range(nums_vertex):
        for i in range(nums_vertex):
            for j in range(nums_vertex):
                if dis[i][j] > dis[i][k] + dis[k][j]:
                    dis[i][j] = dis[i][k] + dis[k][j]
    return dis


print(Floyd(matrix_distance))

"""
    Dijkstra and Bellman-Ford: (單一起點 / 所有終點) Single source to find all the other end's destination
    Floyid : All pairs shortest path
    https://zhuanlan.zhihu.com/p/61628249
    
    Shortest path 問題，極為廣義的weighted directed graph
    => undirected graph 問題 可以用 directed graph 的模板下去解，反之則無法
    => 可以視為 unweighted graph 的 DFS/ BFS 擴充版本
    
    最短路徑一定不包含 cycle, 所以至多只會有 V-1 條 edge
    最短路徑必定是由小段的最短路徑(subpath)所連結起來
    
    處理Single-Source Shortest Path的三種演算法，各別的適用情境與時間複雜度如下：
    (注意：一律不允許negative cycle出現)!!!!

    Bellmam-Ford Algorithm： (一般加權值)
    只要Graph中沒有negative cycle，即使有positive cycle、edge有negative weight，皆可使用。 !!!!
    時間複雜度：O(VE)。
    
    Shortest Path on DAG：
    只要Graph中沒有cycle，即使edge有negative weight，亦可使用。
    時間複雜度：O(V+E)。
    
    Dijkstra's Algorithm：(核心 greedy) (沒有負數邊)
    只要Graph中的edge沒有negative weight，即使有cycle，亦可使用。 !!!
    時間複雜度，根據實現Min-Priority Queue之資料結構將有所不同：
    若使用普通矩陣(array)，需要O(E+V^2)； 
    若使用Binary Heap，需要O((E+V)logV)；
    若使用Fibonacci Heap，只需要O(E+VlogV)。
    講義 6-42, Time Complexity = line20 * (line26 + line33) = O(n) *O(2*n) = O(2*n^2) ~= O(n^2) (記住這個!!!!!!!)
    
    =>(延伸), 因為Bellmend-Ford 和 dijkstra 都是single pair shortest path, therefore both Dijkstra and Bellmend-Ford:
    Time Complexity: O(n^2)
    
    Floyid: (All pair shortest-path)
    Time Complexity: O(n^3) (O(n^2) * n = O(n^3)) (因為就是把所有的single pair 當作輸入乘上每個點 = all pair shortest-path)!!!
    
    有向圖本身用 距離相鄰矩陣來表示
    
    http://alrightchiu.github.io/SecondRound/shortest-pathintrojian-jie.html
    https://www.youtube.com/watch?v=NLp9C7AvJhk
"""
