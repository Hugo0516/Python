class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)

        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])

        return "".join(a)


"""
題意： 假如 k=2, 那就要把字串每4個切開, 然後每4個的前2個要顛倒 !!

Approach 1: Direct

Time Complexity: O(N), where N is the size of s. We build a helper array, plus reverse about half the character in s.
Space Complexity: O(N), the size of a.
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "abcdefg"
    k_1 = 2
    print(demo.reverseStr(input_1, k_1))
