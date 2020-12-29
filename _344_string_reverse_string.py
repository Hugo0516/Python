class Solution:
    def reverseString(self, s):
        s.reverse()


class Solution2:
    def reverseString(self, s):
        def helper(left, right):
            if left < right:
                s[left], s[right] = s[right], s[left]
                helper(left + 1, right - 1)

        helper(0, len(s) - 1)


class Solution3:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


"""
Approach 1: Life is short, use python


Approach 2: Recursion, In-Place, O(N) Space <Divide and Conquer>

Does in-place mean constant space complexity?
No. By definition, an in-place algorithm is an algorithm which transforms input using no auxiliary data structure.

The tricky part is that space is used by many actors, not only by data structures. 
The classical example is to use recursive function without any auxiliary data structures.

Is it in-place? Yes.
Is it constant space? No, because of recursion stack.

Time Complexity: O(N), time to perform N/2 swaps.
Space Complexity: O(N), to keep the recursion stack.

Approach 3: Two Pointers, Iteration, O(1) Space

Time Complexity: O(N), to swap N/2 element
Space Complexity: O(1), it's a constant space solution


"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()
    demo3 = Solution3()

    input_1 = ["h", "e", "l", "l", "o"]
    input_2 = ["h", "e", "l", "l", "o"]
    input_3 = ["h", "e", "l", "l", "o"]

    print(demo.reverseString(input_1))
    print(demo2.reverseString(input_2))
    print(demo3.reverseString(input_3))
