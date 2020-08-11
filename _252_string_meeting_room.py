from typing import List


class Solution:
    def canAttendMeeting(self, intervals: List[List[int]]) -> bool:
        start = []
        end = []
        for lines in intervals:
            start.append(lines[0])
            end.append(lines[1])

        start.sort()
        end.sort()

        for i in range(1, len(start)):
            if start[i] < end[i - 1]:   # 前一個活動還沒結束, 新的人又進來, 導致房間裡有兩個人, 但是房間裡只能有一個人
                return False
        return True


"""
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
    determine if a person could attend all meetings.

    Input: [[0,30],[5,10],[15,20]]
    Output: false
    start = [0, 5, 15] / end = [10, 20, 30]

    Input: [[7,10],[2,4]]
    Output: true

    0-----4
        2----6
     1----4
    --------
    0-----4
    
    與 253 互相參照
    https://www.youtube.com/watch?v=0roQnDBC27o
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[0, 30], [5, 10], [15, 20]]
    print(demo.canAttendMeeting(input_1))
