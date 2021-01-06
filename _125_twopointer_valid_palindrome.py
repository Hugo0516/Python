class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda ch: ch.isalnum(), s)
        lowercase_filtered_chars = map(lambda ch: ch.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]

        return filtered_chars_list == reversed_chars_list


class Solution2:
    def isPalindrome(self, s: str) -> bool:

        i, j = 0, len(s) - 1

        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1

            if s[i].lower() != s[j].lower():
                return False

            i += 1
            j -= 1

        return True


"""
Approach 1: Compare with Reverse

We'll reverse the given string and compare it with the original. If those are equivalent, it's a palindrome.
Since only alphanumeric characters are considered, we'll filter out all other types of characters before we apply our algorithm.
Additionally, because we're treating letters as case-insensitive, we'll convert the remaining letters to lower case. 
The digits will be left the same.

Time Complexity: O(n)
Space Complexity: O(n)

Approach 2: Two Pointers

Time Complexity: O(n)
Space Complexity: O(1)
"""

if __name__ == '__main__':
    demo = Solution()
    demo2 = Solution2()

    input_1 = "A man, a plan, a canal: Panama"
    input_2 = "race a car"

    print(demo.isPalindrome(input_1))
    print(demo2.isPalindrome(input_2))
