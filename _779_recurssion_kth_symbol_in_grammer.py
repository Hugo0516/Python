from collections import deque


class Solution:
    def kthGrammar(self, N: int, K: int) -> int:
        dp = deque([0])
        flag = 1

        while dp:
            if flag == N:
                break
            for i in range(len(dp)):
                if dp[0] == 0:
                    dp.popleft()
                    dp.append(0)
                    dp.append(1)
                else:
                    dp.popleft()
                    dp.append(1)
                    dp.append(0)

            flag += 1

        return dp[K - 1]


class Solution2(object):
    def kthGrammar(self, N, K):
        lastrow = '0'
        while len(lastrow) < N:
            lastrow = "".join('01' if x == '0' else '10'
                              for x in lastrow)
        return int(lastrow[-1][K - 1])


class Solution3(object):
    def kthGrammar(self, N, K):
        if N == 1:
            return 0

        # int ((1-k%2)), k%2 代表我們要知道這個第k個位置, 是奇數還是偶數,
        # 如果 k 是奇數, 然後對應到上一行是 0 的話, k = 0
        # 如果 k 是偶數, 然後對應到上一行是 0 的話, k = 1
        # 如果 k 是奇數, 然後對應到上一行是 1 的話, k = 1
        # 如果 k 是偶數, 然後對應到上一行是 1 的話, k = 0
        # 因為, 0->01, 1->10
        # ^ => XOR, 1,1 or 0,0 = 0

        # self.kthGrammar() = > 代表第 N 行 和 N-1 行的關係
        return int((1 - K % 2)) ^ self.kthGrammar(N - 1, (K + 1) // 2)


class Solution4(object):
    def kthGrammar(self, N, K):
        if N == 1:
            return 0
        if K <= (2 ** (N - 2)):
            return self.kthGrammar(N - 1, K)
        return self.kthGrammar(N - 1, K - 2 ** (N - 2)) ^ 1


class Solution5(object):
    def kthGrammar(self, N, K):
        return bin(K - 1).count('1') % 2


"""
I did it by myself. <Brute Force>
Time Complexity: 幹, 這時間複雜度太高, time limit exceeded !!
Space Complexity:

Approach 2: Brute Force
Time Complexity: O( 2^N )
Space Complexity: O( 2^N )

Approach 3: Recursion (Parent Variant)
*** 記住這一個 ***
Time Complexity: O(N)
Space Complexity: O(1)
解釋: https://www.youtube.com/watch?v=nHW6C64FV_U

Approach 4: Recursion (Flip Variant)
Time Complexity: O(N)
Space Complexity: O(1)

Approach 5: Binary Count
Time Complexity: O(LogN)
Space Complexity: O(1), (In Python, bin(X) creates a string of length O(logX), which could be avoided.) 

"""

if __name__ == '__main__':
    demo = Solution()

    print(demo.kthGrammar(1, 1))
    print(demo.kthGrammar(2, 1))
    print(demo.kthGrammar(2, 2))
    print(demo.kthGrammar(4, 5))
    print('-----')

    demo3 = Solution3()
    print(demo3.kthGrammar(4, 5))

    demo4 = Solution4()
    print(demo4.kthGrammar(4, 5))

    demo5 = Solution5()
    print(demo5.kthGrammar(4, 5))
