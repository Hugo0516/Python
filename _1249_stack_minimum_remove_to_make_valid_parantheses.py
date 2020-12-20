class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()

        stack = []
        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()
        indexes_to_remove = indexes_to_remove.union(set(stack))
        # 要把 stack 裡面剩餘的東西也+進來 set 裡面; 這裡聰明的話你可以用 union, 不然你可以先從 stack pop 出來
        #  然後再 一個一個 add 到 set 裡面
        string_builder = []
        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                string_builder.append(c)
        return "".join(string_builder)


"""
Solution:

Algorithm: Let's put all this together into a 2-parse algorithm.
1. Identify all indexes that should be removed.
2. Build a new string with removed indexes.

As explained above, we should use a stack. If we put the indexes of the "(" on the stack, 
then we'll know that all the indexes on the stack at the end are the indexes of the unmatched "(". 
We should also use a set to keep track of the unmatched ")" we come across. 
Then, we can remove the character at each of those indexes and then return the edited string.

Time Complexity: O(n)
Space Complexity: O(n)

Leetcode 解釋得很好, 還有其他解法, 可是我看 time 沒差, 所以就懶得看了 

和 301 互相參照 !!!

"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "lee(t(c)o)de)"
    print(demo.minRemoveToMakeValid(input_1))

    input_2 = "))(("
    input_3 = "a)b(c)d"
    print(demo.minRemoveToMakeValid(input_2))
    print(demo.minRemoveToMakeValid(input_3))

    input_4 = "L(e)))et((co)d(e"
    print(demo.minRemoveToMakeValid(input_4))
