class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # 1.01 vs 1.001 => 0
        v1 = version1.split('.')
        v2 = version2.split('.')

        max_length = max(len(v1), len(v2))

        for i in range(max_length):
            temp_1 = int(v1[i]) if i < len(v1) else None    # ['1', '01'] , 不要忘記 int()
            temp_2 = int(v2[i]) if i < len(v2) else None    # ['1', '001']

            # if temp_1 > temp_2:
            #     return 1
            # elif temp_2 > temp_1:
            #     return -1
            # else:
            #     if temp_1 is None:
            #         return -1
            #     elif temp_2 is None:
            #         return 1

            if not temp_2 and temp_1:
                return 1
            elif not temp_1 and temp_2:
                return -1
            elif temp_1 and temp_2:
                if temp_1 > temp_2:
                    return 1
                elif temp_2 > temp_1:
                    return -1
        return 0

"""
    Time Complexity: O(max(m, n))   => line 9 取最大！！！
    Space Complexity: O(max(m, n)) => line 10, 11 取最大
"""

if __name__ == '__main__':
    demo = Solution()
    print(demo.compareVersion('1.001', '1.0001'))