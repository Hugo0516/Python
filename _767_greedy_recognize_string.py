import heapq


class Solution:

    def reorganizeString(self, S: str) -> str:
        pq = [(-S.count(x), x) for x in set(S)]
        heapq.heapify(pq)  # O(logA)

        if any(-nc > (len(S) + 1) / 2 for nc, x in pq):
            return ""

        ans = []
        while len(pq) >= 2:  # O(n/2) = O(n)
            nct1, ch1 = heapq.heappop(pq)
            nct2, ch2 = heapq.heappop(pq)
            ans.extend([ch1, ch2])

            if nct1 + 1:
                heapq.heappush(pq, (nct1 + 1, ch1))
            if nct2 + 1:
                heapq.heappush(pq, (nct2 + 1, ch2))

        return "".join(ans) + (pq[0][1] if pq else '')


"""
The task is only impossible if the frequency of a letter exceeds (N+1) / 2. 
Writing the most common letter followed by the second most common letter keeps this invariant.

Core thought: we want to get most frequently characters place it into string 
and then place the next most frequently occurring character right after it, 
we know that would not have any conflict => the two adjacent characters are not the same.

Greedy Part:
wW are greedily taking the most occurring character in the next most frequent character 
and add them into our result.

Reference: https://www.youtube.com/watch?v=zaM_GLLvysw

Time Complexity: O(NlogA), where N is the length of S, and A is the size of the alphabet.
If A is fixed, the complexity is O(N)

Space Complexity: O(A), if A is fixed the complexity would be O(1)

*** 我覺得 時間複雜度 可以再想一下 ***

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "aab"
    input_2 = "aaab"
    input_3 = "aaaabbbcd"

    print(demo.reorganizeString(input_1))
    print(demo.reorganizeString(input_2))
    print(demo.reorganizeString(input_3))
