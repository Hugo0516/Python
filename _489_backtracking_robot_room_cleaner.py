# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
class Robot:
    def move(self):
        """
        Returns true if the cell in front is open and robot moves into the cell.
        Returns false if the cell in front is blocked and robot stays in the current cell.
        :rtype bool
        """

    def turnLeft(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def turnRight(self):
        """
        Robot will stay in the same cell after calling turnLeft/turnRight.
        Each turn will be 90 degrees.
        :rtype void
        """

    def clean(self):
        """
        Clean the current cell.
        :rtype void
        """


class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        def go_back():
            # turn 180 degree to back the former cell
            robot.turnRight()
            robot.turnRight()
            robot.move()
            # turn 180 degree to the initial direction
            robot.turnRight()
            robot.turnRight()

        def backtrack(cell=(0, 0), d=0):
            # d = direction, cell=x,y座標, 這裡用 tuple 表示, 其實不用用tuple 表示也可以
            # 你直接用兩個變數 i, j也行, 他這裡只是故意把他縮減到一個變數而已
            visited.add(cell)
            robot.clean()
            # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
            for i in range(4):
                new_d = (d + i) % 4
                # 假如舊的 d=3 + (1...4), 因為會超過4, 超過4的話我們就沒辦法定位說要用 70 行的哪個 direction
                new_cell = (cell[0] + directions[new_d][0], \
                            cell[1] + directions[new_d][1])

                if not new_cell in visited and robot.move():
                    backtrack(new_cell, new_d)
                    go_back()
                # turn the robot following chosen direction : clockwise
                # 前面 56 ~ 63, 就是指我們在某個方向進行完 dfs 後, 搜索完了之後,
                # 藉由 64 行可以回到"失敗"的前一個 "正確的" initial的 "狀態"
                # 然後回到 initial 狀態後, 在藉由 68 行 開始 clockwise, 做下一個方向的搜索
                robot.turnRight()

        # going clockwise : 0: 'up', 1: 'right', 2: 'down', 3: 'left'
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()
        backtrack()


"""
     x
    1o 3o
    2o
    => 舉例：我們現在往上搜索(2o往x), 到達 x 之後, 會因為 62 行, 所以無法繼續下去,
    那就會回到上一層 recursion, 回到上一層後就會藉由 64 行, 回到1o的初始位置
    回到 1o 的初始位置後, 可以在藉由 69 行, 往 3o 的地方開始搜索
    
    
This is a classic backtracking problem

可以聽這個解說： https://www.youtube.com/watch?v=y4izHfShEfU

Time Complexity: O(N - M), where N is a number of cells in the room and M is a number of obstacles.
We visit each non-obstacle cell once and only once.
At each visit, we will check 4 directions around the cell. Therefore, the total number of operations would be 4⋅(N−M).

Space Complexity: O( N - M ), where N is a number of cells in the room and M is a number of obstacles.
We employed a hashtable to keep track of whether a non-obstacle cell is visited or not.

"""

if __name__ == '__main__':
    demo = Solution()
    room = [
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 1],
        [0, 0, 0, 1, 0, 0, 0, 0],
        [1, 1, 1, 1, 1, 1, 1, 1]
    ]
    row = 1
    col = 3
    print(demo.cleanRoom())
