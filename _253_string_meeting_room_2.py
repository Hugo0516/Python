from typing import List


class Solution:
    def minMeetingRoom(self, intervals: List[List[int]]) -> int:
        start = []
        end = []
        room = 0
        for lines in intervals:
            start.append(lines[0])
            end.append(lines[1])

        start.sort()
        end.sort()
        endpoint = 0

        for i in range(0, len(start)):
            if start[i] < end[endpoint]:
                room += 1

            else:
                endpoint += 1
        return room


"""
    Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei),
    find the minimum number of conference rooms required.
    [0, 5, 15] / [10, 20, 30]
    
    0-----5-------15
    ----------10--------20-----30
        (2)         (1)     (1)     room
        
    [2, 7] / [4, 10]
    
    --2-----7
    ----4-------10
     (1)    (1)         room
    
    與 252 互相參照
    https://www.youtube.com/watch?v=0roQnDBC27o
"""

if __name__ == '__main__':
    demo = Solution()
    input_1 = [[0, 14], [5, 10], [15, 16]]
    input_2 = [[7, 10], [2, 4]]
    print(demo.minMeetingRoom(input_1))
    print(demo.minMeetingRoom(input_2))

