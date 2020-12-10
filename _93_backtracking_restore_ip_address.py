from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def valid(segment):
            """
            Check if the current segment is valid :
            1. less or equal to 255
            2. the first character could be '0'
               only if the segment is equal to '0'
            """
            return int(segment) <= 255 if segment[0] != '0' else len(segment) == 1

        def update_output(curr_pos):
            """
            Append the current list of segments
            to the list of solutions
            """
            segment = s[curr_pos + 1:n]
            if valid(segment):
                segments.append(segment)
                output.append('.'.join(segments))
                segments.pop()

        def backtrack(prev_pos=-1, dots=3):
            """
            prev_pos : the position of the previously placed dot
            dots : number of dots to place
            """
            # The current dot curr_pos could be placed
            # in a range from prev_pos + 1 to prev_pos + 4.
            # The dot couldn't be placed
            # after the last character in the string.
            for curr_pos in range(prev_pos + 1, min(n - 1, prev_pos + 4)):
                segment = s[prev_pos + 1:curr_pos + 1]
                if valid(segment):
                    segments.append(segment)  # place dot
                    if dots - 1 == 0:  # if all 3 dots are placed
                        update_output(curr_pos)  # add the solution to output
                    else:
                        backtrack(curr_pos, dots - 1)  # continue to place dots
                    segments.pop()  # remove the last placed dot

        n = len(s)
        output, segments = [], []
        backtrack()
        return output


class Solution2(object):
    def restoreIpAddresses(self, s):
        res = []
        self.dfs(s, [], res)
        return res

    def dfs(self, s, path, res):
        x, y = len(s), 4 - len(path)
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            res.append('.'.join(path))
            return
        for i in range(min(3, len(s))):
            curr = s[:i + 1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            self.dfs(s[i + 1:], path + [s[:i + 1]], res)


class Solution3:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) > 12 or len(s) < 4:
            return []

        outputList = []

        def helper(startingIndex=0, count=1, string=''):

            for index in range(startingIndex, startingIndex + 3, 1):
                newString = s[startingIndex: index + 1]
                if len(newString) > 1 and newString[0] == '0':
                    break
                if int(newString) > 255:
                    break
                restString = s[index + 1:]
                if len(restString) < 4 - count:
                    break
                if len(restString) > (4 - count) * 3:
                    continue
                if count == 4:
                    outputList.append(string + newString)
                    break
                helper(index + 1, count + 1, string + newString + '.')

        helper()
        return outputList


class Solution4:
    def restoreIpAddresses(self, s):
        def dfs(s, sub, ips, ip):
            if sub == 4:  # should be 4 parts
                if s == '':
                    ips.append(ip[1:])  # remove first '.'
                return

            for i in range(1, 4):  # the three ifs' order cannot be changed!
                if i <= len(s):  # if i > len(s), s[:i] will make false!!!!
                    if int(s[:i]) <= 255:
                        dfs(s[i:], sub + 1, ips, ip + '.' + s[:i])
                    if s[0] == '0':
                        break  # make sure that res just can be '0.0.0.0' and remove like '00'

        ips = []
        dfs(s, 0, ips, '')
        return ips


class Solution5(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        self.helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]

    # k 代表剩下幾組 / temp 代表中間過程暫時數組
    def helper(self, ans, s, remain_octet, temp):
        _ = 1  # 加這行只是因為我要在 debug mode 下可以看到完整 debug 資訊; 所以這行毫無意義
        if len(s) > remain_octet * 3:  # every octet can have maximum 3 digits
            # 這一個判斷式, 是為了加快判斷速度
            return
        if remain_octet == 0 and len(s) == 0:
            ans.append(temp[:])
            # ans += temp[:]
        else:
            x = len(s) - remain_octet + 1
            for i in range(min(3, len(s) - remain_octet + 1)):
                # len(s) - k + 1, 因為k代表剩餘octet數, 所以假設最後剩餘k組裡面都只放一個數字;
                # 因為怕會overflow, 所以用 min(), 至於 + 1是因為我們用的是 range 所以要+1
                # EX: 假設現在 k = 2, 代表說我們目前正在進行定二組 octet 的helper, 所以呈現這樣 => 以決定.進行中.剩下1.剩下2
                # 那剩下的兩組假設只需要滿足最低限度個擺一個數字即可的話, 那代表說 我在進行中可以用的最大數組為 len(s) - 2
                # 但是, 因為我們是用 range 所以加一, => len(s) - 2 + 1
                # 但是, 因為實際上我們 octet 裡面只能擺最多三個數字, => min(3, len(s) - k + 1)
                if i == 2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                    _ = 3
                    continue
                    # return 我在想這裡把 continue 改成 return 好像更合理
                self.helper(ans, s[i + 1:], remain_octet - 1, temp + [s[:i + 1]])


"""
Time complexity : as discussed above, there is not more than 27 combinations to check.
Space complexity : constant space to keep the solutions, not more than 19 valid IP addresses.

我覺得這一題難在要怎麼定義清楚他的正確定義, 
EX: 0.0.0.0 (o), 但 01.23.34.66 (x) / 每一組 octet 不能>255

記住 Solution5, 其他的太難懂

Reference:
Approach 1 : Leetcode official 
Approach 2: 負雪
Approach 3: Leetcode 路人
Approach 4: https://www.cnblogs.com/zuoyuan/p/3768112.html
Approach 5: https://leetcode.com/problems/restore-ip-addresses/discuss/30946/DFS-in-Python

Time Complexity: 3^n
Since, 每個數字最多會跑 for 3 次, EX: 你要確定 2.x.x.x / 25.x.x.x / 255.x.x.x 哪個是否正確 => 你的 "2" 就要跑三次 for
Space Complexity: 3^n ( 因為 recursion call (stack) )

Input: s = "25525511135"
Output: ["255.255.11.135","255.255.111.35"]
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = "25525511135"
    input_2 = "0000"
    input_3 = "1111"

    input_4 = "010010"
    input_5 = "101023"

    print(demo.restoreIpAddresses(input_1))
    print(demo.restoreIpAddresses(input_2))
    print(demo.restoreIpAddresses(input_3))
    print(demo.restoreIpAddresses(input_4))
    print(demo.restoreIpAddresses(input_5))

    demo2 = Solution2()
    print(demo2.restoreIpAddresses(input_1))

    demo3 = Solution3()
    print(demo3.restoreIpAddresses(input_1))

    demo4 = Solution4()
    print(demo4.restoreIpAddresses(input_1))

    demo5 = Solution5()
    print(demo5.restoreIpAddresses(input_1))
