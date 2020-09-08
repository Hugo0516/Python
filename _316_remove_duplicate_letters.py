import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        count = collections.Counter(s)
        stack = []
        visited = collections.defaultdict(bool)
        for c in s:
            count[c] -= 1
            if visited[c]:
                continue
            while stack and count[stack[-1]] and stack[-1] > c:
                visited[stack[-1]] = False
                stack.pop()
            visited[c] = True
            stack.append(c)
        return "".join(stack)



"""
https://www.youtube.com/watch?v=SrlvMmfG8sA
"""
if __name__ == '__main__':
    demo = Solution()
    print(demo.removeDuplicateLetters("bcabbc"))
