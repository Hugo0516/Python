class UnionFindSet:

    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]  # 一開始每個結點的 parent 都為他自己 => 代表每一個點都是獨立的node
        # 也就是說 假如n = 5, 那麼現在就有5個forest的感覺,且每個forest就是只有一個node(所以此node也等於此樹的root)
        self._ranks = [1 for i in range(n + 1)]  # 因為上面一行的初始,所以rank 設成0(我覺得或許與可以設成1??)

    def find(self, u):  # 返回 u 的主先
        while u != self._parents[u]:  # 表示 u 不是根結點
            self._parents[u] = self._parents[self._parents[u]]  # 順便做 pass compression
            u = self._parents[u]
        return u

    def union(self, u, v):
        root_x, root_y = self.find(u), self.find(v)
        if root_x == root_y:
            return False

        if self._ranks[root_x] < self._ranks[root_y]:
            self._parents[root_x] = root_y
        elif self._ranks[root_x] > self._ranks[root_y]:
            self._parents[root_y] = root_x
        else:
            self._parents[root_y] = root_x  # 假如 rank 相同, 將 pv 放到 pu 底下
            self._ranks[root_x] += 1

        return True


"""
    Union Find可用於解決集合相關問題，如判斷某元素是否屬於集合、兩個元素是否屬同一集合、求解集合個數等
    Weighting和Path compression兩種方法可以同時使用，這樣使得對N個元素進行M次Union Find操作的時間複雜度可以減少到(M+N)lgN。
    因lgN隨N的增長變化很小，所以整體算法時間複雜度接近於線性的時間複雜度。
    
    684 和 737 為此類型的經典應用！！！！！！
    
    Union Find 的題目好像雞戶都可以用 DFS 的概念下去解
    
    Disjoint-set/Union-find Forest

    Find(x): find the root/cluster-id of x
    
    Union(x, y): merge two clusters
    
    Check whether two elements are in the same set or not in O(1)*.
    
    Find: O(ɑ(n))* ≈ O(1)
    
    Union: O(ɑ(n))* ≈ O(1)
    
    Space: O(n)
    
    Without optimization: Find: O(n)
    
    Two key optimizations:
    
    1. Path compression: make tree flat
    2. Union by rank: merge low rank tree to high rank one
    *: amortized (上面的 * 都代表 平攤結果)
    
    ɑ(.): inverse Ackermann function
    --------------------------------------------------------------------
    https://zxi.mytechroad.com/blog/data-structure/sp1-union-find-set/
"""
