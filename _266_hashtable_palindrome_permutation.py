import collections


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        _l = len(s)
        _dict = collections.defaultdict(int)

        for item, value in enumerate(s):
            _dict[value] += 1

        odd, even = 0, 0

        if _l % 2 == 0:
            for v in _dict.values():
                if v % 2 != 0:
                    return False
        else:
            for v in _dict.values():
                if odd == 2:
                    return False
                if v % 2 != 0:
                    odd += 1

        return True


"""
If a string with an even length is a palindrome, 
every character in the string must always occur an even number of times. 

If the string with an odd length is a palindrome, 
every character except one of the characters must always occur an even number of times. 

=> Finished by myself

Time Complexity: O(n), n = length of string
Space Complexity: O(1), The map can grow up to a maximum number of all distinct elements.
However, the number of distinct characters are bounded, so as the space complexity.
"""

if __name__ == '__main__':
    pass
